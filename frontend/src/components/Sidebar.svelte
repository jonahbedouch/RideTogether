<script lang="ts">
	import X from "../icons/X.svelte";
import { backendStore } from "../stores/backend";
let sidebar: boolean;

backendStore.subscribe(value => {
    sidebar = value.sidebar;
})
</script>

<div class="absolute h-full transition-[width] z-10 bg-oxford-blue-900 overflow-hidden {sidebar ? 'w-full' : 'w-0'}">
    <div class="flex flex-col text-baby-powder-50">
        <div class="flex w-full m-4 align-middle items-center justify-center">
            <button class="mr-auto" on:click={backendStore.toggleSidebar}>
                <X></X>
            </button>
            <img class="h-12 transition-none absolute self-center" src="/text_logo_pink.png" alt="Ride Together Logo"/>
        </div>
        <button class="text-3xl py-5 border-t-2 border-t-oxford-blue-300">
            Profile
        </button>
        <button class="text-3xl py-5 border-t-2 border-t-oxford-blue-300">
            History
        </button>
        <button class="text-3xl py-5 border-t-2 border-t-oxford-blue-300">
            Log out
        </button>
    </div>
</div>