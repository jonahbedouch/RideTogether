<script lang="ts">
import mapboxgl from 'mapbox-gl'; // or "const mapboxgl = require('mapbox-gl');"
	import { onMount } from 'svelte';

mapboxgl.accessToken = 'pk.eyJ1Ijoiam9uYWhiZWRvdWNoIiwiYSI6ImNsZHBoNXpxaTBsZWMzeG52aDduaG9hNWEifQ.TGxSVcKU9aN2ZgdNGfThkA';
let map: mapboxgl.Map;

const success = (pos: GeolocationPosition) => {
  const crd = pos.coords;

  console.log('Your current position is:');
  console.log(`Latitude : ${crd.latitude}`);
  console.log(`Longitude: ${crd.longitude}`);
  console.log(`More or less ${crd.accuracy} meters.`);

  map.setCenter([crd.longitude, crd.latitude]);
  map.setZoom(12);
}

const error = (err: GeolocationPositionError) => {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

onMount(() => {
    map = new mapboxgl.Map({
        container: 'map', // container ID
        style: 'mapbox://styles/mapbox/dark-v11', // style URL
        center: [-74.5, 40], // starting position [lng, lat]
        zoom: 5, // starting zoom
    });

    navigator.geolocation.getCurrentPosition(success, error,
        {enableHighAccuracy: false, timeout: 5000, maximumAge: 10});
})
</script>

<div id="map" class="w-full h-full"></div>