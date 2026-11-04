"""Content blocks reused across several plan PDFs (trains, toy train, flights, vehicles, Airbnb, gear)."""

GROUP = 6  # travellers

# ---------------------------------------------------------------- calendar
CALENDAR = [
    ["Date", "Day", "What it means"],
    ["24 Dec 2026", "Thursday", "Start. 12285 Duronto (Sun/Thu) and 17005 Hyderabad–Raxaul (Thu only) both run today."],
    ["25 Dec", "Friday", "Christmas. Most trains from Telangana reach Delhi this morning. Red Fort is open (closed Mondays)."],
    ["26 Dec", "Saturday", "Weekend crowds in Shimla/Manali/Mussoorie. Nathula usually open (closed Mon/Tue)."],
    ["31 Dec", "Thursday", "New Year's Eve. Airbnb rates peak; 2–3 night minimum stays are common for 30 Dec–1 Jan."],
    ["1 Jan 2027", "Friday", "Heavy traffic down from the hills. 12286 Duronto NZM→SC runs (Mon/Fri)."],
    ["2 Jan", "Saturday", "Leave Delhi: 12724 Telangana Exp 16:00 or 22692 Rajdhani (late evening) → home 3 Jan."],
    ["3 Jan", "Sunday", "Must be home. Keep it as buffer only."],
]

BOOKING_WINDOW = [
    ["Journey date", "General booking opened (60-day rule)", "Tatkal (day before)"],
    ["24 Dec 2026 (onward)", "25 Oct 2026 (open now)", "23 Dec: 10:00 AC / 11:00 SL"],
    ["25 Dec (Delhi → Kalka / Jammu / Amritsar)", "26 Oct 2026 (open now)", "24 Dec 10:00 / 11:00"],
    ["1 Jan 2027", "2 Nov 2026 (open now)", "31 Dec 10:00 / 11:00"],
    ["2 Jan 2027 (return)", "3 Nov 2026 (open since yesterday)", "1 Jan 10:00 / 11:00"],
]
PNR_NOTE = ("<b>6 people = 1 PNR in general quota</b> (max 6 passengers per ticket), but <b>Tatkal allows only 4 per PNR</b>, so Tatkal "
            "needs 2 bookings from 2 Aadhaar-verified IRCTC accounts at the same minute. Senior citizens get lower berths only in general quota.")

# ---------------------------------------------------------------- onward trains (Hyderabad / Kazipet / Warangal / Vijayawada)
ONWARD_TRAINS = [
    ["Train", "Where you board (time)", "Reaches Delhi", "Runs", "Fare / person (SL · 3A)", "Use it for"],
    ["<b>12723 Telangana SF Exp</b>", "<b>Hyderabad Deccan 06:00</b> · Secunderabad 06:20/06:25 · Kazipet 08:03/08:05",
     "New Delhi ~07:40–08:00 (25 Dec)", "Daily", "≈ ₹800 · ≈ ₹2,100", "<b>Default.</b> Cheapest, boards in the city. Delhi day + night train/bus onward"],
    ["<b>12621 Tamil Nadu SF Exp</b>", "Vijayawada 03:50–04:05 · Warangal 06:50/06:52 · <b>Kazipet 06:55</b>",
     "New Delhi <b>06:30</b> (25 Dec)", "Daily", "≈ ₹750 · ≈ ₹1,950 (from Kazipet)", "<b>Fast option.</b> Catches the 07:40 Kalka Shatabdi → Shimla same evening"],
    ["<b>22691 Bengaluru–Nizamuddin Rajdhani</b>", "Secunderabad 07:00/07:10 · Kazipet ~08:50", "H. Nizamuddin 05:30", "Daily",
     "3A ≈ ₹3,300–4,100 (meals incl.)", "Fast and comfortable but ~2× the 3A fare"],
    ["12625 Kerala SF Exp", "Vijayawada ~10:10–10:55 · Warangal ~13:30 · <b>Kazipet 13:45</b>", "New Delhi 13:30", "Daily",
     "≈ ₹750 · ≈ ₹1,950", "Backup if 12723 is full (leave Hyderabad by 09:30 by bus)"],
    ["12285 Secunderabad–Nizamuddin Duronto", "Secunderabad 12:50", "H. Nizamuddin ~10:40", "Sun &amp; Thu", "3A ≈ ₹3,000–3,700",
     "Runs on 24 Dec (Thu)"],
    ["12615 Grand Trunk Exp", "Vijayawada ~01:00–02:00 · Kazipet 04:00 (very early 24 Dec)", "New Delhi 05:10", "Daily",
     "≈ ₹750 · ≈ ₹1,950", "Only if you can leave Hyderabad around midnight"],
    ["12721 Dakshin SF Exp", "Hyderabad Deccan 23:00 · Kazipet ~01:15", "H. Nizamuddin ~03:45 on 26 Dec", "Daily", "≈ ₹780 · ≈ ₹2,100",
     "Evening departure; costs you a day"],
    ["<b>17005 Hyderabad–Raxaul Exp</b>", "Hyderabad Deccan <b>23:10</b> · Secunderabad 23:30", "— (Raxaul, Nepal border ~17:00 Sat 26 Dec)",
     "<b>Thu only</b>", "≈ ₹870 · ≈ ₹2,300", "<b>Nepal plan</b>"],
    ["Weekly via Kacheguda: 12647 Kongu, 12649/12629 K. Sampark Kranti, 12781 Swarna Jayanti", "Kacheguda (times vary)", "H. Nizamuddin",
     "1–2× a week", "SL / 3A", "Check if one runs on 24 Dec"],
]
TO_KAZIPET = ("<b>Getting to Kazipet / Warangal / Vijayawada with 6 people:</b> Kazipet and Warangal are ~140 km (2.5–3 h). TGSRTC buses "
              "run through the night from JBS/Uppal to Hanamkonda (≈ ₹200–300), or an Innova one-way ≈ ₹4,000–5,000 (≈ ₹750 pp). "
              "Vijayawada is ~275 km (5–6 h). Only worth it if Hyderabad quota is full, because you'd need an overnight bus on 23 Dec.")

TELANGANA_HALTS = (
    "<b>12723 halts in order (check availability to each):</b> Hyderabad Deccan → Secunderabad → Kazipet → Ramagundam → Mancherial → "
    "Sirpur Kagaznagar → Balharshah → Chandrapur → Sevagram → Nagpur → Itarsi → Bhopal → Jhansi → Gwalior → Agra Cantt → New Delhi "
    "(~18 halts, ~1,680 km). Confirmed: HYB 06:00, SC 06:20/06:25, Kazipet 08:03/08:05, Ramagundam 09:28/09:30."
)

HALT_METHOD = [
    "<b>1. Direct pairs.</b> On IRCTC / ConfirmTkt / ixigo, search 24 Dec: HYB→NDLS, SC→NDLS, SC→NZM, <b>KZJ→NDLS, WL→NDLS, BZA→NDLS</b> "
    "(Kazipet, Warangal and Vijayawada have their own quotas). Note AVAILABLE / RAC / WL for every train above.",
    "<b>2. Every halt.</b> If HYB→Delhi is WL, search the same train from HYB to each later halt (Agra Cantt, Gwalior, Jhansi, Bhopal, "
    "Itarsi, Nagpur). A shorter ticket can be AVAILABLE when the full one is WL. Ride to Agra, then any Agra→Delhi train or bus (2–3.5 h).",
    "<b>3. Book from the origin.</b> For trains starting elsewhere (22691 from Bengaluru, 12621 from Chennai, 12625 from Thiruvananthapuram), "
    "search origin→Delhi and set <b>Boarding Point</b> = Secunderabad / Kazipet / Warangal / Vijayawada. You pay the full-route fare but get the origin's quota.",
    "<b>4. Split it.</b> HYB→Nagpur + Nagpur→Delhi (30+ trains a day). Keep 2–3 h between them.",
    "<b>5. Tatkal on 23 Dec</b> (AC 10:00, SL 11:00), 2 PNRs of 3 people each. Premium Tatkal costs more but confirms more often.",
    "<b>6. Tick Vikalp + auto-upgrade</b> and only hold WL if it is under ~WL 20 (3A) / WL 40 (SL) this far out.",
]

# ---------------------------------------------------------------- Delhi → Kalka → toy train
DELHI_KALKA = [
    ["If you arrive in Delhi on…", "Delhi → Kalka", "Kalka → Shimla (toy train)", "In Shimla", "Buffers", "Train cost / person"],
    ["<b>12723 Telangana</b> · New Delhi ~07:40 (25 Dec)", "<b>12311 Netaji (Kalka Mail)</b>, Old Delhi ~21:10 → Kalka ~03:00–04:40 (SL)",
     "<b>52453 Kalka–Shimla Exp</b> ~06:00–06:20 (2S ≈ ₹65) or 52451 Shivalik Deluxe ~05:20–05:45 (CC ≈ ₹510)",
     "~10:30–11:50 on 26 Dec", "~13 h in Delhi = a sightseeing day; 1–3 h in Kalka waiting room", "<b>≈ ₹265</b> (SL ≈ ₹200 + 2S ₹65)"],
    ["<b>12621 Tamil Nadu</b> · New Delhi 06:30", "<b>12011 Kalka Shatabdi</b>, New Delhi 07:40 → Kalka 11:40–11:45 (CC ≈ ₹885 incl. meal)",
     "<b>52455 Himalayan Queen</b> 11:55–12:10 → ~17:20 (CC ≈ ₹265; 2S cheaper)", "~17:20 on <b>25 Dec</b>", "70 min at New Delhi (fog risk), "
     "~25 min at Kalka (timed connection)", "≈ ₹1,150"],
    ["22691 Rajdhani · Nizamuddin 05:30", "Same 12011 Shatabdi (Nizamuddin → New Delhi 15–20 min by metro/cab)", "52455 Himalayan Queen",
     "~17:20 on 25 Dec", "~2 h at Delhi", "≈ ₹1,150"],
    ["12625 Kerala · New Delhi 13:30", "12311 Kalka Mail ~21:10 (or 12005 Kalka Shatabdi 17:15 → 21:15 + a night in Kalka)", "52453 / 52451 next morning",
     "~11:00 on 26 Dec", "~7.5 h Delhi", "≈ ₹265"],
]
DELHI_KALKA_NOTE = ("Late-December fog regularly delays trains from the south by 1–4 h. If the fast option misses the 07:40 Shatabdi, "
                    "fall back to the Kalka Mail at night: you lose half a day, not the trip. Book the Shatabdi only after checking the "
                    "Tamil Nadu Express running status the evening before (Tatkal opens 10:00 on 24 Dec).")

TOY_TRAIN = [
    ["Direction", "Train", "Departs", "Arrives", "Classes &amp; approx fare", "Notes"],
    ["Kalka → Shimla", "52457 Kalka–Shimla (earliest)", "~03:30", "~08:55", "2S / FC", "Listed by some 2026 guides. Verify; may be seasonal"],
    ["Kalka → Shimla", "72451 Rail Motor Car", "05:10–05:25", "~09:30", "≈ ₹320", "Glass-roof railcar, 14–18 seats; runs only with enough bookings"],
    ["Kalka → Shimla", "52451 Shivalik Deluxe", "05:20–05:45", "~10:05–10:40", "CC ≈ ₹510 (breakfast incl.)", "Fastest regular train"],
    ["Kalka → Shimla", "<b>52453 Kalka–Shimla Exp</b>", "06:00–06:20", "~11:05–11:50", "<b>2S ≈ ₹65</b>; FC higher", "Cheapest reserved seat"],
    ["Kalka → Shimla", "52455 Himalayan Queen", "11:55–12:10", "~17:20", "2S cheap · CC ≈ ₹265 · FC ≈ ₹475", "Connects with the 12011 Shatabdi"],
    ["Shimla → Kalka", "52456 Himalayan Queen", "10:40", "16:10", "As above", "Connects to evening Delhi trains"],
    ["Shimla → Kalka", "52458 Passenger", "14:20–14:25", "~20:10", "2S / FC", ""],
    ["Shimla → Kalka", "52452 Shivalik Deluxe", "17:40–17:50", "~22:25–22:45", "CC ≈ ₹510", "Connects to the overnight Kalka Mail to Delhi"],
    ["Shimla → Kalka", "52454 Kalka–Shimla Exp", "18:25–18:30", "~23:20–23:30", "2S ≈ ₹65", ""],
]
TOY_NOTE = ("Timings differ by 10–25 min between sources (travelcoffee 2026, Shimla Tourism, exploreindia, totaltraininfo). Confirm on IRCTC/NTES "
            "when you book. Book toy-train seats on IRCTC as soon as the main train is confirmed; 25–26 Dec sells out. "
            "Sit on the right side going up for the valley views. The Him Darshan Vistadome (≈ ₹630) runs on some dates.")

# ---------------------------------------------------------------- return trains
RETURN_TRAINS = [
    ["Train", "Leaves", "Reaches Hyderabad", "Runs", "Fare (SL · 3A)", "Fits 'home by 3 Jan'?"],
    ["<b>12724 Telangana SF Exp</b>", "New Delhi <b>16:00</b>", "Hyderabad Deccan ~17:10 next day", "Daily", "≈ ₹800 · ≈ ₹2,100",
     "<b>Leave 2 Jan → home 3 Jan evening</b>"],
    ["<b>22692 Nizamuddin–Bengaluru Rajdhani</b>", "H. Nizamuddin late evening (≈ 20:30–21:00, verify)", "Secunderabad 17:10 arr next day",
     "Daily", "3A ≈ ₹3,300–4,100", "Leave 2 Jan → home 3 Jan"],
    ["12286 Nizamuddin–Secunderabad Duronto", "H. Nizamuddin 15:55", "Secunderabad ~14:35 next day", "Mon &amp; Fri", "3A ≈ ₹3,000–3,700",
     "Leave 1 Jan (Fri) → home 2 Jan"],
    ["12722 Dakshin SF Exp", "H. Nizamuddin 22:50", "Hyderabad Deccan ~03:50 on day 3", "Daily", "≈ ₹780 · ≈ ₹2,100",
     "Leave 1 Jan night → home 3 Jan 04:00"],
    ["<b>12792 Danapur–Secunderabad SF Exp</b>", "Danapur (Patna) <b>12:15</b>", "Secunderabad ~21:30 next day", "Daily",
     "≈ ₹840 · ≈ ₹2,200", "<b>Nepal plan</b>: leave 2 Jan → home 3 Jan night"],
    ["17006 Raxaul–Hyderabad", "Raxaul 03:15", "Hyderabad Deccan 19:40 next day", "Sun only", "≈ ₹870 · ≈ ₹2,300",
     "No: 3 Jan departure reaches 4 Jan"],
]

# ---------------------------------------------------------------- flights
FLIGHTS = [
    ["Route (non-stop)", "Airlines", "Flight time", "Typical Dec–Jan one-way fare*", "Useful for"],
    ["Hyderabad ↔ Delhi", "IndiGo, Air India, Akasa, SpiceJet", "~2 h 10 m", "₹6,000–9,000 (peak ₹10–12k)", "Plans 1, 2, 3, 5, 6, 7"],
    ["Hyderabad → Chandigarh", "IndiGo (≈2 daily)", "~2 h 30 m", "₹7,000–9,500", "Plans 1, 2, 7 (Kalka is 25 km from IXC)"],
    ["Hyderabad ↔ Srinagar", "IndiGo, Air India Express", "~3 h", "₹9,600–11,100 (peak to ~₹15,700)", "Plan 3"],
    ["Hyderabad ↔ Bagdogra", "IndiGo (+ Air India Express)", "~2 h 20 m", "₹6,500–8,500 (peak ₹9–12k)", "Plan 4"],
    ["Hyderabad ↔ Dehradun", "IndiGo (~10 flights/week)", "~2 h 25 m", "₹5,000–9,000", "Plan 5"],
]
FLIGHT_NOTE = ("*Snapshot ranges from MakeMyTrip, Goibibo, Skyscanner, HappyFares, ixigo (Nov 2026), not live quotes. IndiGo: 7 kg cabin + 15 kg "
               "check-in on most fares. Fares climb weekly from here for 24 Dec and 2 Jan.")

# ---------------------------------------------------------------- vehicles for 6
VEHICLES = [
    ["Option for 6 people", "Seats / luggage", "Typical hill rate (2025–26)", "Per person per day (÷6)", "When to choose"],
    ["<b>Innova Crysta</b> with driver", "6–7 + roof carrier", "₹4,000–5,500/day (min ~250 km) or ₹16–18/km, + tolls, parking, ₹300–500 driver night",
     "≈ ₹750–1,000", "Default for 6 with soft bags"],
    ["Tempo Traveller 12-seater", "Lots of room", "₹4,500–7,500/day or ₹18–22/km", "≈ ₹850–1,250", "Heavy luggage; not allowed on some narrow roads / union areas"],
    ["2 × Dzire / Etios", "4 + 4", "₹2,800–3,500/day each", "≈ ₹950–1,150", "Only if no SUV is available"],
    ["Local taxi unions (Manali, Pahalgam, Gangtok, Joshimath)", "Innova / Tavera / Sumo", "Fixed rate cards per circuit", "Varies", "Mandatory for some circuits (Solang–Sissu, Aru–Betaab, Tsomgo)"],
    ["Government bus (HRTC / JKSRTC / UTC)", "Seats", "₹1.5–3 per km", "Cheapest", "Long point-to-point legs (Shimla→Manali, Delhi→hills)"],
]

# ---------------------------------------------------------------- Airbnb
AIRBNB_HOWTO = [
    "<b>Filters:</b> Guests = 6 · Type of place = <b>Entire home</b> · Bedrooms ≥ 3 (or 2 + sofa-beds) · tick <b>Guest favourite</b> · toggle "
    "<b>'Display total before taxes'</b> so the price includes cleaning and service fees.",
    "<b>Best-rated vs cheapest:</b> sort by price after setting the filters, then pick the cheapest listing with ≥ 4.7★ and ≥ 20 reviews. A 5.0★ "
    "with 3 reviews is not more reliable than a 4.8★ with 150.",
    "<b>Winter questions to message the host before booking:</b> room heaters (some charge ₹300–500/night per heater), geyser/hot water, power "
    "backup, whether a car reaches the door (Old Manali, Vashisht, Jibhi and McLeodganj often have steep stairs), and snow-time access.",
    "<b>NYE rules:</b> many hosts set a 2–3 night minimum for 30 Dec–1 Jan. Book those nights first with flexible or moderate cancellation.",
    "<b>Where Airbnb is thin</b> (Zuluk, Aritar, Rinchenpong, Sari/Chopta, Sangla/Kalpa, Bandipur, Spiti), book homestays by phone or on "
    "Booking.com / MakeMyTrip. Usually 3 rooms × ₹1,500–3,000 with meals.",
]
AIRBNB_NOTE = ("Listing names, ratings and review counts come from Airbnb search results in Nov 2026. Airbnb blocks automated price checks, so the "
               "'Dec price for 6' column is an <b>estimate</b> for an entire 3-bedroom place over the holiday week. Check the live total for your dates.")

# ---------------------------------------------------------------- international
INTERNATIONAL = [
    ["Destination", "How", "Main cost driver", "Realistic per person (6 people, 24 Dec–3 Jan)", "Verdict"],
    ["<b>Nepal</b> (Kathmandu, Bandipur, Pokhara)", "17005 Hyderabad→Raxaul (Thu 23:10) · walk into Birgunj · back via Patna + 12792",
     "Trains ~₹1,700 SL total; no visa (passport or voter ID)", "<b>≈ ₹19–28k</b> (shoestring–recommended)", "<b>Fits. Full plan included (Plan 8)</b>"],
    ["Bhutan (Thimphu, Punakha, Paro)", "Fly HYD→Bagdogra + 160 km to Phuentsholing", "SDF ₹1,200/person/night + flights ₹13–17k + Bhutan car",
     "≈ ₹40–46k", "Over budget"],
    ["Sri Lanka", "IndiGo / SriLankan direct HYD–CMB", "Return flights ₹21–35k in Dec", "≈ ₹38–50k", "Over budget"],
    ["Thailand", "IndiGo / Thai / Nok direct HYD–BKK", "Return flights from ~₹27k (mid-Dec); higher at Christmas. Visa-free rules changing in 2026",
     "≈ ₹45–55k", "Over budget"],
    ["Malaysia", "AirAsia / Malaysia Airlines direct HYD–KUL", "One-way ₹14–18k at Christmas; visa-free only till 31 Dec 2026", "≈ ₹45–55k", "Over budget"],
    ["Vietnam", "Connecting flights + e-visa (~US$25)", "Flights ₹18–22k+", "≈ ₹45–55k", "Over budget"],
]

OTHER_NORTH = [
    ["Also considered (North India)", "Why it is not a full plan"],
    ["Spiti in winter (Kaza, Langza, Hikkim, Key, Chicham)", "Reachable only via Kinnaur in winter. Needs ~8 days from Shimla plus 2 train days each way, "
     "so it doesn't fit 24 Dec–3 Jan without a flight back. Most homestays close; −20 °C nights. Operator packages ₹24–36k + travel. Plan 7 "
     "covers Kinnaur (the lower half of the same road)."],
    ["Ladakh in winter", "Fly-in only (Delhi–Leh ₹5–9k each way + HYD–DEL); −15 to −25 °C; 2 acclimatisation days. ≈ ₹38–45k."],
    ["Mussoorie–Landour–Dhanaulti", "Easy and cheap but little snow in late Dec. Listed as a variant inside Plan 5."],
    ["Kumaon (Nainital, Mukteshwar, Munsiyari)", "Good alternative to Plan 5. Munsiyari is 10–11 h beyond Kathgodam. Listed as a variant in Plan 5."],
]

# ---------------------------------------------------------------- winter gear
GEAR_TABLE = [
    ["Item", "Need", "Buy (Decathlon Hyderabad / local)", "Rent (where &amp; rate)", "Advice"],
    ["Thermal inner set (top + bottom) ×2", "Must", "₹800–1,200 per set (local ₹400–600)", "Not rented (hygiene)", "Buy. Merino/poly, not cotton"],
    ["Fleece / sweater (mid layer)", "Must", "₹600–1,200", "—", "Buy"],
    ["Padded / down jacket (−5 to −10 °C)", "Must", "₹2,500–5,000", "Indiahikes rentals ₹55–80/day (ships to you); trek operators ₹100/day; "
     "Manali / Gulmarg shops ₹150–300/day", "Rent if you won't reuse it: 10 days ≈ ₹600–1,000"],
    ["One-piece snow suit", "Snow points", "—", "Solang/Palchan, Kufri, Gulmarg, Tsomgo ₹250–500/day (often with gumboots)", "Rent on the spot"],
    ["Gumboots / snow boots", "Snow points", "—", "₹100–200/day (bundled with suit at Solang ₹400–500)", "Rent on the spot"],
    ["Waterproof trekking shoes", "Treks", "₹2,000–3,500 (Decathlon MH100/MH500)", "Trek operators ₹100–150/day", "Buy if you'll trek again"],
    ["Waterproof gloves + woollen inners", "Must", "₹300–900 + ₹150", "—", "Buy"],
    ["Woollen cap / balaclava / neck gaiter", "Must", "₹200–400 each", "—", "Buy"],
    ["Woollen socks (4 pairs)", "Must", "₹400–600", "—", "Buy"],
    ["UV400 sunglasses", "Snow", "₹300–800", "—", "Prevents snow-blindness"],
    ["Microspikes + gaiters", "Treks / icy walks", "₹1,200–1,800", "Chopta/Sari/Sankri/Dharamkot ₹150–250/day; gaiters ₹100/day", "Rent"],
    ["Trekking pole", "Treks", "₹400–700", "₹50–100/day", "Rent"],
    ["Ski kit", "Optional", "—", "Gulmarg ≈ ₹700/day + jacket ₹300 + trouser ₹200; Solang/Auli lesson ₹1,000–2,500", "Optional"],
    ["Cold cream, SPF 50, lip balm, hand-warmers", "Must", "₹500–700 total", "—", "Buy"],
]
GEAR_SUMMARY = ("<b>Gear budget:</b> if you own nothing warm, expect ₹4,000–6,500 one-time purchase (thermals, fleece, gloves, cap, socks, "
                "sunglasses) + ₹800–1,500 rentals on the trip. Plan budgets include only the rentals. Six people can share: buy 2 pairs of microspikes "
                "and 1 first-aid kit for the group instead of 6.")

PACKING = [
    "Original photo ID (Aadhaar/DL) + 2 photocopies + <b>4 passport photos</b> each (Sikkim/Bhutan permits, J&amp;K checks). "
    "<b>Nepal: passport or voter ID</b> (Aadhaar is generally not accepted).",
    "Power bank (cold halves battery life), offline maps, ₹5–8k cash each (ATMs fail in snow areas).",
    "Group med kit: paracetamol, ORS, cold/cough tablets, band-aids, Vaseline, motion-sickness tablets (hill roads). Diamox only on a doctor's advice.",
    "Thermos for hot water, quick-dry towel, plastic bags for wet gear, a 3-pin multi-plug for the Airbnb (one socket per room is common).",
    "Prepaid SIMs from outside J&amp;K don't work in Kashmir. Carry at least 2 postpaid connections in the group (Plan 3).",
]

COMMON_SAFETY = [
    "Roads and snow change by the hour. Check state police traffic updates and ask your host each evening. Emergency: <b>112</b>. HP disaster helpline: <b>1077</b>.",
    "No two-wheelers on fresh snow or black ice. Taxis with chains are safer after snowfall.",
    "Book 30 Dec–1 Jan stays first (NYE rates 2–3×). Prefer flexible cancellation.",
    "Start the last long leg (hills → Delhi/railhead) by 1 Jan. NYE traffic and snow delay buses 3–8 h.",
]

HELPFUL_DELHI_DAY = [
    "<b>Delhi day on 25 Dec (Friday, Christmas): luggage + Old Delhi circuit.</b> From New Delhi station take the Yellow Line 2 stops to Chandni Chowk. "
    "Leave bags at the Delhi Jn (Old Delhi) cloak room (≈ ₹30–60 per bag per day; bags must be locked).",
    "<b>Red Fort</b> (₹35 Indians, opens 09:30, closed Mondays) → <b>Jama Masjid</b> → <b>Chandni Chowk</b> food (Paranthe Wali Gali, Old Famous "
    "Jalebi Wala) → <b>Gurudwara Sis Ganj</b>. Then the Metro to Central Secretariat for <b>Kartavya Path / India Gate</b>, <b>Agrasen ki Baoli</b>, "
    "<b>Connaught Place</b>. Christmas evening service at <b>Sacred Heart Cathedral</b>. Back at Old Delhi by 20:30.",
    "Cost ≈ ₹600–900 pp (metro day pass ₹200, entries, food). Christmas crowds are heavy at CP and India Gate after 17:00.",
]
