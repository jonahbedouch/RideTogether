<script lang="ts">
	import mapboxgl from 'mapbox-gl'; // or "const mapboxgl = require('mapbox-gl');"
	import { onMount } from 'svelte';
	import { locationStore } from '../stores/location';

	mapboxgl.accessToken =
		'pk.eyJ1Ijoiam9uYWhiZWRvdWNoIiwiYSI6ImNsZHBoNXpxaTBsZWMzeG52aDduaG9hNWEifQ.TGxSVcKU9aN2ZgdNGfThkA';
	let map: mapboxgl.Map;

	onMount(() => {
		map = new mapboxgl.Map({
			container: 'map', // container ID
			style: 'mapbox://styles/mapbox/dark-v11', // style URL
			center: [-83.810306, 39.923152], // starting position [lng, lat]
			zoom: 1 // starting zoom
		});

		// Add geolocate control to the map.
		const geolocate = new mapboxgl.GeolocateControl({
			positionOptions: {
				enableHighAccuracy: true
			},
			// When active the map will receive updates to the device's location as it changes.
			trackUserLocation: true,
			// Draw an arrow next to the location dot to indicate which direction the device is heading.
			showUserHeading: true
		});
		map.addControl(geolocate);
        
        map.on('load', () => {
            geolocate.trigger();
        })
	});
</script>

<div id="map" class="w-full h-full" />
