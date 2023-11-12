from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from . import models


# Create your views here.
@login_required
def update_location(request):
    try:
        user_profile = models.Profile.objects.get(user=request.user)
        if not user_profile:
            raise ValueError("Can't get User details")
        point = request.POST["point"].split(",")
        point = [float(part) for part in point]
        point = Point(point, srid=4326)
        user_profile.last_location = point
        user_profile.save()
        return JsonResponse({"message": f"Set location to {point.wkt}."}, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)
