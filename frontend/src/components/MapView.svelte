<script lang="ts">
	import mapboxgl, { Marker, type LngLatLike } from 'mapbox-gl'; // or "const mapboxgl = require('mapbox-gl');"
	import { onMount } from 'svelte';
	import { driveStore } from '../stores/drive';
	import { locationStore } from '../stores/location';

    let marker1: Marker;
    let marker2: Marker;

	export let drive = false;

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

			if (drive) {
				driveStore.subscribe((value) => {
                    if (map.getLayer('route')) {
                        map.removeLayer('route');
                    }

                    if (map.getSource('route')) {
                        map.removeLayer('route');
                    }

                    if (marker1) {
                        marker1.remove();
                    }

                    if (marker2) {
                        marker2.remove();
                    }

					map.addLayer({
						id: 'route',
						type: 'line',
						source: {
							type: 'geojson',
							data: {
								type: 'Feature',
								properties: {},
								geometry: {
									type: 'LineString',
									coordinates: value.original_route
								}
							}
						},
						layout: {
							'line-join': 'round',
							'line-cap': 'round'
						},
						paint: {
							'line-color': '#3b4f68',
							'line-width': 8
						}
					});

					marker1 = new mapboxgl.Marker({ color: '#84bc9c', rotation: 0 }).setLngLat([value.start_dest[1], value.start_dest[0]]).addTo(map);

					marker2 = new mapboxgl.Marker({ color: '#84bc9c', rotation: 0 })
						.setLngLat([value.end_dest[1], value.end_dest[0]])
						.addTo(map);
				});
			}
		});
	});
</script>

<div id="map" class="w-full h-full" />
