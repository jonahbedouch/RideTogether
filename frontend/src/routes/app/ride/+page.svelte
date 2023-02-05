<script lang="ts">
    import BottomBar from "../../../components/BottomBar.svelte";
	import MapView from "../../../components/MapView.svelte";
	import RideCard from "../../../components/RideCard.svelte";
	import TopBar from "../../../components/TopBar.svelte";
</script>

<div class="w-full h-screen flex flex-col">
    <TopBar></TopBar>
    <MapView></MapView>
    <RideCard></RideCard>
</div>
