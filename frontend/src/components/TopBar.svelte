<script lang="ts">
	import Menu from "../icons/Menu.svelte";
	import { backendStore } from "../stores/backend";
</script>

<div class="flex w-full h-16 bg-zomp-300 align-middle items-center justify-center">
    <button class="h-16 mx-4 text-white mr-auto" on:click={backendStore.toggleSidebar}>
        <Menu></Menu>
    </button>
    <img class="h-12 absolute self-center" src="/text_logo.png" alt="Ride Together Logo"/>
</div>