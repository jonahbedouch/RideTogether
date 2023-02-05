<script lang="ts">
	import DriveCard from "../../../components/DriveCard.svelte";
    import MapView from "../../../components/MapView.svelte";
	import TopBar from "../../../components/TopBar.svelte";
</script>

<div class="w-full h-screen flex flex-col">
    <TopBar></TopBar>
    <MapView drive={true}></MapView>
</div>

<div class="absolute w-full bottom-0">
    <DriveCard></DriveCard>
</div>
