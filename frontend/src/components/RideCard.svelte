<script>
	import { rideStore } from '../stores/ride';

	$: focusedSession = $rideStore.sessions[$rideStore.selectedSession] ?? null;
</script>

{#if focusedSession}
	<div class="h-96 m-8 p-4 flex flex-col bg-oxford-blue-900 text-baby-powder-50 rounded-xl">
		<div class="flex flex-row">
			<h1 class="mr-auto text-2xl">{focusedSession.driver}'s Session</h1>
			<button class="bg-oxford-blue-600 p-2 rounded-xl">Cancel</button>
		</div>

		{#each [...Array(focusedSession.passengers_max).keys()] as num}
			{#if focusedSession.passengers && focusedSession.passengers[num]}
				<p class="my-2">{focusedSession.passengers[num]}</p>
			{:else}
				<p class="my-2">Waiting for a user to join...</p>
			{/if}
		{/each}
	</div>
{/if}
