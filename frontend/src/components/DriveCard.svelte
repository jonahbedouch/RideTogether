<script>
	import { driveStore } from "../stores/drive";

</script>
<div class="h-96 m-8 p-4 flex flex-col bg-oxford-blue-900 text-baby-powder-50 rounded-xl">
    <div class="flex flex-row">
        <h1 class="mr-auto text-2xl">Your Session</h1>
        <button class="bg-oxford-blue-600 p-2 rounded-xl">Cancel</button>
    </div>
    {#each [...Array($driveStore.passengers_max).keys()] as num}
        {#if ($driveStore.passengers && $driveStore.passengers[num])}
            <p class="my-2">{ $driveStore.passengers[num] }</p>
        {:else}
            <p class="my-2">Waiting for a user to join...</p>
        {/if}
    {/each}
</div>