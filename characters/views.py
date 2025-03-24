import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Character, Location
from .forms import CharacterForm, LocationForm

def home(request):
    return render(request, 'characters/home.html')

def about(request):
    return render(request, 'characters/about.html')

def index(request):
    return render(request, 'characters/index.html')

def fetch_characters(request):
    url = "https://rickandmortyapi.com/api/character"
    try:
        response = requests.get(url)
        response.raise_for_status()
        try:
            data = response.json()
        except ValueError as e:
            return JsonResponse({"error": f"Erro ao decodificar JSON: {str(e)}"}, status=500)
        characters = data.get("results", [])
        saved_count = 0
        locations_count = {}
        for character in characters:
            location_data = character["location"]
            location_id = location_data["url"].split("/")[-1] if location_data["url"] else 0
            if location_id not in locations_count:
                locations_count[location_id] = 0
            locations_count[location_id] += 1
            location, created = Location.objects.update_or_create(
                api_id=location_id,
                defaults={"name": location_data["name"]},
            )
            _, created = Character.objects.update_or_create(
                api_id=character["id"],
                defaults={
                    "name": character["name"],
                    "status": character["status"],
                    "species": character["species"],
                    "type": character["type"],
                    "gender": character["gender"],
                    "origin_name": character["origin"]["name"],
                    "location_name": character["location"]["name"],
                    "image": character["image"],
                    "location": location,
                },
            )
            if created:
                saved_count += 1
        for location_id, count in locations_count.items():
            Location.objects.filter(api_id=location_id).update(residents_count=count)
        return JsonResponse({"message": f"{saved_count} personagens salvos com sucesso!"}, status=201)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Erro ao buscar dados: {str(e)}"}, status=500)

def character_list(request):
    search_term = request.GET.get('search', '')
    if search_term:
        characters = Character.objects.filter(name__icontains=search_term)
    else:
        characters = Character.objects.all()
    return render(request, 'characters/character_list.html', {'characters': characters, 'search_term': search_term})

def character_create(request):
    form = CharacterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('character-list')
    return render(request, 'characters/character_form.html', {'form': form})

def character_update(request, pk):
    character = get_object_or_404(Character, pk=pk)
    form = CharacterForm(request.POST or None, instance=character)
    if form.is_valid():
        form.save()
        return redirect('character-list')
    return render(request, 'characters/character_form.html', {'form': form, 'character': character})

def character_delete(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == "POST":
        character.delete()
        return redirect('character-list')
    return render(request, 'characters/character_confirm_delete.html', {'character': character})

def location_list(request):
    search_term = request.GET.get('search', '')
    if search_term:
        locations = Location.objects.filter(name__icontains=search_term)
    else:
        locations = Location.objects.all()
    for location in locations:
        location.residents = location.characters.all()
    return render(request, 'characters/location_list.html', {'locations': locations, 'search_term': search_term})

def location_create(request):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('location-list')
    return render(request, 'characters/location_form.html', {'form': form})

def location_update(request, pk):
    location = get_object_or_404(Location, pk=pk)
    form = LocationForm(request.POST or None, instance=location)
    if form.is_valid():
        form.save()
        return redirect('location-list')
    return render(request, 'characters/location_form.html', {'form': form, 'location': location})

def location_delete(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == "POST":
        location.delete()
        return redirect('location-list')
    return render(request, 'characters/location_confirm_delete.html', {'location': location})