import type { LngLatLike } from "mapbox-gl";

export interface session {
    driver: number;
    end_dest: [number, number];
    id: number;
    original_route: Array<LngLatLike>;
    passengers?: Array<number>;
    passengers_max: number;
    start_dest: [number, number];
    timestamp: number;
}