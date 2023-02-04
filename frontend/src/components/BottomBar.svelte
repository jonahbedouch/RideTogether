<script lang="ts">
	import MapPin from "../icons/MapPin.svelte";
	import UserPlus from "../icons/UserPlus.svelte";

    
</script>

<div class="w-full bg-zomp-300 border-t-4 border-zomp-50 h-24 flex flex-row">
    <button class="flex flex-col items-center justify-center w-full text-center text-baby-powder-50 border-r-2 border-zomp-50">
        <MapPin></MapPin>
        <span class="font-medium">Drive</span>
    </button>
    <button class="flex flex-col items-center justify-center w-full text-center text-baby-powder-50 border-l-2 border-zomp-50">
        <UserPlus></UserPlus>
        <span class="font-medium">Join</span>
    </button>
</div>
