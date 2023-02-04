<script>
	import 'mapbox-gl/dist/mapbox-gl.css';
	import { onMount } from 'svelte';
	import '../app.css';
	import { locationStore } from '../stores/location';

    onMount(() => {
        if (navigator.geolocation) {
            navigator.geolocation.watchPosition(locationStore.success, locationStore.error ,
                {enableHighAccuracy: false, timeout: 5000, maximumAge: 10});
        }
    })
</script>

<slot />