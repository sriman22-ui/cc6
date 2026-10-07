# Solar Journey 3D – interactive concept (handover)

Interactive Three.js diorama for the CC0006 showcase: NTU EEE building with a
split roof (left = hot roof today, right = biosolar roof proposal) and the
Campus Loop bus stop with a Today / Solar Cool Stop switch. Built for a laptop
at the booth: mouse / trackpad drag to orbit, scroll to zoom, click to explore.

## Files
- index.html – the whole scene + UI (Three.js 0.160, plain JS, no build step)
- views.json – the agreed camera views (stops 1–4 + overview) and the clip script
- shoot2.mjs – Playwright script that renders stills / tour frames (still works)
- comp3.py – builds the photo-vs-3D comparison images (Pillow)
- reference-photos/ – EEE building, NTU rooftop solar, Campus Loop bus stop, campus bus

## Run locally
    npm install            # three + playwright
    npm start              # python3 -m http.server 8765
    open http://localhost:8765/index.html

The page must be served over http (the importmap and views.json fetch need it).
If views.json cannot be loaded the page falls back to an inline copy of the views.

## What's interactive
- Continuous render loop + OrbitControls (damped, 6–150 units zoom, never below ground, pan clamped to the site)
- Hotspot pins 1–4 and the tour-bar steps are clickable: 1.2 s eased camera tween to that stop's view from views.json, info card appears
- ‹ › Prev / Next buttons (cycle overview → 1 → 2 → 3 → 4 → overview)
- ▶ guided tour: 8 s per stop, pause/resume button; any drag, scroll or click stops it. Stop 4 shows Today first, then flips to the Solar Cool Stop
- Bus-stop switch (top right) animates Today ↔ Solar Cool Stop (shrink / pop-in)
- Ceiling fans spin, heat arrows rise and fade, evapotranspiration arrows drift
- ⟲ Reset view returns to the overview
- Campus Loop bus (NTU blue shuttle, from reference-photos/campus-bus.png) drives in, stops at the shelter and drives off every 10 s
- Keyboard: ← → stops, 1–4 jump to a stop, space play/pause, Esc or Home reset, T toggles the bus stop

## Key places in index.html
- Camera views + which view each stop uses: search "STOP_VIEW"
- EEE building: search "EEE building"
- Roof halves: search "roof halves" (conv[] = hot roof, bio[] = biosolar; animated arrows in heatArrows / evapArrows)
- Bus stop: search "Campus Loop bus stop" (stopToday / stopProp inside the todayP / propP pivot groups)
- Bus: search "Campus Loop bus" (busX() is the 10 s timing profile)
- Info-card text: CARDS; tour labels: steps; hotspot positions: HS
- Tour / tween / toggle logic: search "state", "guided tour", "render loop"
- Timings: HOLD (seconds per stop), TWEEN (camera move), FLIP_AFTER (Today → Solar Cool Stop delay at stop 4), BUS_T

## window API (used by shoot2.mjs, handy from the console)
setStep(n), setMode('today'|'proposal'), setCam(p,t), setUI(bool), showPins(bool),
hideCard(), draw(dt), goTo(n), startTour(), stopTour(), state(), setBusT(seconds)

## Still to confirm with the group
- Which building is in the rooftop-solar reference photo
- Whether the EEE roof really has panels (or move the pilot roof)
- Exact name of the Campus Loop bus stop
