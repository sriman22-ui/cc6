# Solar Journey 3D – interactive concept (handover)

Interactive Three.js diorama for the CC0006 showcase: NTU EEE building with a
fully biosolar roof (panels raised above low-growing plants) and the Campus
Loop bus stop rebuilt as the Solar Cool Stop. Built for a laptop at the booth:
mouse / trackpad drag to orbit, scroll to zoom, click to explore.

## Files
- index.html – the whole scene + UI (Three.js 0.160, plain JS, no build step)
- views.json – the agreed camera views (overview, stop 1, stop 2, under canopy) and the clip script
- shoot2.mjs – Playwright script that renders stills / tour frames (still works)
- comp3.py – builds the photo-vs-3D comparison images (Pillow)
- reference-photos/ – EEE building, NTU rooftop solar, Campus Loop bus stop, campus bus
- assets/ntu-logo.png – NTU logo (trimmed), used on the bus

## Run locally
    npm install            # three + playwright
    npm start              # python3 -m http.server 8765
    open http://localhost:8765/index.html

The page must be served over http (the importmap and views.json fetch need it).
If views.json cannot be loaded the page falls back to an inline copy of the views.

## What's interactive
- Continuous render loop + OrbitControls (damped, 6–150 units zoom, never below ground, pan clamped to the site)
- Trackpad friendly: two-finger swipe orbits, pinch zooms; click-drag orbits and a mouse wheel zooms too
- Hotspot pins 1–2 and the tour-bar steps are clickable: 1.2 s eased camera tween to that stop's view from views.json, info card appears
- ‹ › Prev / Next buttons (cycle overview → 1 Biosolar roof → 2 Solar Cool Stop → overview)
- ▶ guided tour: 8 s per stop, pause/resume button; any drag, scroll or click stops it
- Ceiling fans spin, evapotranspiration arrows rise and drift
- ⟲ Reset view returns to the overview
- Campus Loop bus (NTU blue shuttle with the NTU logo, from reference-photos/campus-bus.png) drives in, opens its door, waits 4 s at the shelter and drives off; one pass every ~18 s
- Ten students in the "Student Vol 01" outfits: they walk to the stop, wait (standing and on the bench), board, alight and walk away, all in sync with the bus
- Solar Cool Stop appliances are labelled (reused panels, ceiling fans, LED lighting, phone charging, battery) with wiring and moving energy pulses from the canopy
- Keyboard: ← → stops, 1–2 jump to a stop, space play/pause, Esc or Home reset

## Key places in index.html
- Camera views + which view each stop uses: search "STOP_VIEW"
- EEE building: search "EEE building"
- Biosolar roof: search "biosolar roof" (bio group; animated arrows in evapArrows)
- NTU logo panel on the bus: search "logoPanel"
- Bus stop: search "Campus Loop bus stop" (stopProp group)
- Bus: search "Campus Loop bus" (busX() is the timing profile; BUS_V = cruise speed, BUS_WAIT = dwell at the shelter, X_STOP = where it parks)
- Students: search "students" (OUTFITS = colours per model, agents = one schedule per student built with sched(); times are relative to ARR / DEP, the bus arrival and departure)
- Appliance labels + pulses: search "what the canopy panels power" (POWER = labels, ROUTES = wiring)
- Info-card text: CARDS; tour labels: steps; hotspot positions: HS
- Tour / tween / toggle logic: search "state", "guided tour", "render loop"
- Timings: HOLD (seconds per stop), TWEEN (camera move), BUS_V / BUS_WAIT / BUS_GAP (bus cycle), WALK (student walking speed)

## window API (used by shoot2.mjs, handy from the console)
setStep(n), setCam(p,t), setUI(bool), showPins(bool), setMode() (no-op, kept for old scripts),
hideCard(), draw(dt), goTo(n), startTour(), stopTour(), state(), setBusT(seconds)

## Design decisions (current)
- Whole EEE roof is biosolar (no hot-roof half, no roof toggle)
- No "what's underneath" stop or exploded cutaway
- Bus stop shows only the final Solar Cool Stop (no Today state or switch)

## Models
The students are built procedurally in the ten outfits of the "Student Vol 01" sheet (only a preview image was available). If the actual GLB/FBX files turn up they can replace makeStudent() while keeping the same schedules.

## Still to confirm with the group
- Which building is in the rooftop-solar reference photo
- Whether the EEE roof really has panels (or move the pilot roof)
- Exact name of the Campus Loop bus stop
