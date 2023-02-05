<script>
	import 'mapbox-gl/dist/mapbox-gl.css';
	import '../app.css';
	import { onMount } from 'svelte';
	import Sidebar from '../components/Sidebar.svelte';
	import { locationStore } from '../stores/location';
	import Drive from '../components/Drive.svelte';
	import Ride from '../components/Ride.svelte';

    onMount(() => {
        if (navigator.geolocation) {
            navigator.geolocation.watchPosition(locationStore.success, locationStore.error ,
                {enableHighAccuracy: false, timeout: 5000, maximumAge: 10});
        }
    })
</script>

<Sidebar></Sidebar>
<Drive></Drive>
<Ride></Ride>
<slot />