<script lang="ts">
	import MapPin from "../icons/MapPin.svelte";
	import UserPlus from "../icons/UserPlus.svelte";

    
</script>

<div class="w-full bg-zomp-300 border-t-4 border-zomp-50 h-24 flex flex-row">
    <button class="flex flex-col items-center justify-center w-full text-center text-white border-r-2 border-zomp-50">
        <MapPin></MapPin>
        <span>Drive</span>
    </button>
    <button class="flex flex-col items-center justify-center w-full text-center text-white border-l-2 border-zomp-50">
        <UserPlus></UserPlus>
        <span>Join</span>
    </button>
</div>
