"""Content blocks reused across several plan PDFs (trains, flights, gear, booking tips)."""

# ---------------------------------------------------------------- calendar
CALENDAR = [
    ["Date", "Day", "What it means"],
    ["24 Dec 2026", "Thursday", "Start day. 12285 Duronto (Sun/Thu) runs today. 12437 Rajdhani does not (Wed only)."],
    ["25 Dec", "Friday", "Christmas. Hill stations fill up. Most HYD trains reach Delhi this morning."],
    ["31 Dec", "Thursday", "New Year's Eve. Peak hotel rates, long jams near Manali/Solang/Atal Tunnel."],
    ["1 Jan 2027", "Friday", "12286 Duronto NZM→SC runs today (Mon/Fri). Heavy traffic coming down from the hills."],
    ["2 Jan", "Saturday", "Best day to leave Delhi: 12724 Telangana Exp 16:00 or 22692 Rajdhani reaches Hyderabad 3 Jan."],
    ["3 Jan", "Sunday", "Must be home. Keep this day as a buffer only."],
]

BOOKING_WINDOW = [
    ["Journey date", "General booking opened (60-day rule)", "Tatkal opens (day before)"],
    ["24 Dec 2026 (onward)", "25 Oct 2026 (already open)", "23 Dec: 10:00 AM (AC) / 11:00 AM (SL)"],
    ["1 Jan 2027 (return)", "2 Nov 2026 (already open)", "31 Dec: 10:00 / 11:00 AM"],
    ["2 Jan 2027 (return)", "3 Nov 2026 (opened yesterday, book today)", "1 Jan: 10:00 / 11:00 AM"],
]

# ---------------------------------------------------------------- onward trains
ONWARD_TRAINS = [
    ["Train", "Boards in Hyderabad", "Reaches", "Runs", "Classes · approx fare / person", "Use on 24 Dec?"],
    ["<b>12723 Telangana SF Exp</b>", "Hyderabad Deccan (Nampally) <b>06:00</b> · Secunderabad 06:20/06:25",
     "New Delhi ~07:40–08:00 next day (~25.5 h)", "Daily", "SL ≈ ₹800 · 3A ≈ ₹2,100 · 2A ≈ ₹3,000",
     "<b>Yes, best early-morning train</b>"],
    ["<b>22691 Bengaluru–Nizamuddin Rajdhani</b>", "Secunderabad <b>07:00 arr / 07:10 dep</b> (10-min halt)",
     "H. Nizamuddin ~05:30 next day (~22 h)", "Daily", "3A ≈ ₹3,300–4,100 · 2A ≈ ₹4,500–5,500 (flexi fare, meals incl.)",
     "Yes. Fastest morning option"],
    ["22705 Tirupati–Jammu Tawi Humsafar", "Secunderabad ~08:40", "Delhi Safdarjung, then Jammu Tawi",
     "Weekly (sources say Tue from Tirupati, so Wed at SC)", "3A ≈ ₹3,300–3,900 (to Jammu)",
     "Probably 23 Dec, not 24th. Verify. Useful for Plan 3"],
    ["<b>12285 Secunderabad–Nizamuddin Duronto</b>", "Secunderabad <b>12:50</b>", "H. Nizamuddin ~10:40 next day (~22 h)",
     "<b>Sun &amp; Thu</b>", "AC only · 3A ≈ ₹3,000–3,700 (meals incl.)", "<b>Yes, 24 Dec is a Thursday</b>"],
    ["12437 Secunderabad–Nizamuddin Rajdhani", "Secunderabad 12:50", "H. Nizamuddin 10:30 next day", "Wed only",
     "3A ≈ ₹3,300–4,000", "No (23 Dec only)"],
    ["12707 AP Sampark Kranti", "Kacheguda ~16:30", "H. Nizamuddin next day", "Mon/Wed/Fri (verify)",
     "SL / 3A / 2A", "No (not Thursday)"],
    ["12721 Dakshin SF Exp", "Hyderabad Deccan 23:00", "H. Nizamuddin ~03:45 on day 3 (~29 h)", "Daily",
     "SL ≈ ₹780 · 3A ≈ ₹2,100", "Only as a 23-Dec-night fallback (slow)"],
    ["Weekly via Kacheguda: 12647 Kongu, 12649 / 12629 Karnataka Sampark Kranti, 12781 Swarna Jayanti",
     "Kacheguda (times vary)", "H. Nizamuddin", "1–2× a week", "SL / 3A / 2A",
     "Check if any runs on 24 Dec"],
]

ONWARD_BACKUP = [
    ["Fallback station", "Distance from Hyderabad", "Daily Delhi trains you can board there (check availability from here too)"],
    ["Kazipet Jn / Warangal", "~140 km · 2–2.5 h by road, or ride 12723 itself", "12625 Kerala Exp, 12621 Tamil Nadu Exp, 12615 GT Exp, "
     "20805 AP Exp, 12723 Telangana Exp (Kazipet 08:03)"],
    ["Ramagundam", "~210 km", "12723 (09:28), 12625, 12621 and others on the Grand Trunk route"],
    ["Nagpur", "Flight HYD–NAG ~1 h, or bus overnight", "30+ Delhi-bound trains a day. Last resort if everything from Telangana is full"],
]

TELANGANA_HALTS = (
    "<b>12723 major halts, in order (check availability to each):</b> Hyderabad Deccan → Secunderabad → Kazipet → Ramagundam → "
    "Mancherial → Sirpur Kagaznagar → Balharshah → Chandrapur → Sevagram → Nagpur → Itarsi → Bhopal → Jhansi → "
    "Gwalior → Agra Cantt → New Delhi (about 18 halts in total, ~1,680 km). Confirmed times: HYB 06:00, SC 06:20/06:25, "
    "Kazipet 08:03/08:05, Ramagundam 09:28/09:30. Read the other times off NTES or IRCTC on the day."
)

HALT_METHOD = [
    "<b>Step 1. Direct pairs.</b> On IRCTC (or ConfirmTkt / ixigo, same data), search 24 Dec for HYB→NDLS, SC→NDLS, SC→NZM, "
    "HYB→NZM in 3A and SL. Note the status for each train: AVAILABLE / RAC / WL number.",
    "<b>Step 2. Every halt (as you asked).</b> If HYB/SC→Delhi shows WL, search the same train from <b>HYB</b> to each later halt: "
    "Agra Cantt, Gwalior, Jhansi, Bhopal, Itarsi, Nagpur. Seats are split into quotas by distance, so a shorter "
    "ticket (e.g. HYB→Agra) can be AVAILABLE while HYB→Delhi is WL. If Agra/Gwalior is available, book it, ride to Agra "
    "(about 4 h before Delhi), then take any Agra→Delhi train, Gatimaan/Vande Bharat or bus (2–3.5 h, ₹300–800).",
    "<b>Step 3. Book from the train's origin.</b> For trains that start outside Hyderabad (22691 Rajdhani from Bengaluru, "
    "22705 Humsafar from Tirupati), search <b>origin→Delhi</b> (SBC→NZM, TPTY→NZM/Jammu) and set <b>Boarding Point = "
    "Secunderabad</b>. You pay the full-route fare, but the origin's general quota is often open when the Secunderabad quota is full.",
    "<b>Step 4. Board further up the line.</b> Check the same trains from Kazipet / Ramagundam (table above). You can book "
    "HYB→Delhi and board at SC, but you cannot board <i>before</i> the boarding station on your ticket.",
    "<b>Step 5. Split journey.</b> HYB→Nagpur (many trains, short) + Nagpur→Delhi (30+ trains, incl. Rajdhanis from the south). "
    "Leave at least 2–3 h for the change.",
    "<b>Step 6. Tatkal on 23 Dec.</b> AC Tatkal opens 10:00 AM, sleeper 11:00 AM. You need an Aadhaar-authenticated IRCTC "
    "account (OTP). Log in at 9:55 with saved passenger lists and UPI ready. Premium Tatkal costs more but is easier to get.",
    "<b>Step 7. Tick 'Vikalp' and 'auto-upgradation'</b> when booking a WL ticket. Book WL only if the WL number is low "
    "(roughly under WL 20 in 3A, 40 in SL, 50 days out). Otherwise fall back to flights (next table).",
]

# ---------------------------------------------------------------- return trains
RETURN_TRAINS = [
    ["Train", "Leaves", "Reaches Hyderabad", "Runs", "Approx fare (3A)", "Fits 'home by 3 Jan'?"],
    ["<b>12724 Telangana SF Exp</b>", "New Delhi <b>16:00</b>", "Hyderabad Deccan ~17:10 next day", "Daily", "≈ ₹2,100 (SL ≈ ₹800)",
     "<b>Leave 2 Jan → home 3 Jan evening</b>"],
    ["<b>22692 Nizamuddin–Bengaluru Rajdhani</b>", "H. Nizamuddin late evening (≈20:30–21:00, verify)",
     "Secunderabad 17:10 arr / 17:25 dep next day", "Daily", "≈ ₹3,300–4,100", "<b>Leave 2 Jan → home 3 Jan 17:10</b>"],
    ["12286 Nizamuddin–Secunderabad Duronto", "H. Nizamuddin 15:55", "Secunderabad ~14:35 next day", "Mon &amp; Fri",
     "≈ ₹3,000–3,700", "Leave 1 Jan (Fri) → home 2 Jan"],
    ["12722 Dakshin SF Exp", "H. Nizamuddin 22:50", "Hyderabad Deccan ~03:50 on day 3", "Daily", "≈ ₹2,100",
     "Leave 1 Jan night → home 3 Jan 04:00"],
    ["12438 Nizamuddin–Secunderabad Rajdhani", "H. Nizamuddin 15:35", "Secunderabad 13:40 next day", "Sunday only",
     "≈ ₹3,300–4,000", "No (3 Jan departure is too late)"],
    ["22706 Jammu Tawi–Tirupati Humsafar", "Jammu Tawi 05:45", "Secunderabad ~18:00 next day", "Weekly (verify day)",
     "≈ ₹3,300–3,900", "Only Plan 3, and only if it runs 1 Jan"],
]

# ---------------------------------------------------------------- flights
FLIGHTS = [
    ["Route (non-stop)", "Airlines", "Flight time", "Typical Dec–Jan one-way fare*", "Useful for"],
    ["Hyderabad ↔ Delhi", "IndiGo, Air India, Akasa, SpiceJet (many daily)", "~2 h 10 m", "₹6,000–9,000 (24 Dec / 2 Jan can touch ₹10–12k)", "Plans 1, 2, 3, 5"],
    ["Hyderabad → Chandigarh", "IndiGo (≈2 daily)", "~2 h 30 m", "₹7,000–9,500", "Plans 1 &amp; 2 (Shimla is 3–4 h from IXC)"],
    ["Hyderabad ↔ Srinagar", "IndiGo, Air India Express", "~3 h", "₹9,600–11,100 (peak days up to ~₹15,700)", "Plan 3"],
    ["Hyderabad ↔ Bagdogra", "IndiGo (+ Air India Express)", "~2 h 15 m–2 h 30 m", "₹6,500–8,500 (peak ₹9–12k)", "Plan 4"],
    ["Hyderabad ↔ Dehradun", "IndiGo (≈10 flights/week, ~10:25 dep on some days)", "~2 h 25 m", "₹5,000–9,000", "Plan 5"],
]
FLIGHT_NOTE = ("*Snapshot ranges from MakeMyTrip, Goibibo, Skyscanner, HappyFares and ixigo pages seen in Nov 2026, not live quotes. "
               "IndiGo cabin bag: 7 kg; check-in 15 kg on most fares. Winter jackets count, so wear the heaviest layers on the plane. "
               "Book within the next 1–2 weeks: Christmas/New Year fares on these routes usually climb steadily.")

# ---------------------------------------------------------------- winter gear
GEAR_TABLE = [
    ["Item", "Need", "Buy (Decathlon Hyderabad / local)", "Rent (where &amp; rate)", "Advice"],
    ["Thermal inner set (top + bottom) ×2", "Must", "₹800–1,200 per set (local ₹400–600)", "Not rented (hygiene)", "Buy. Merino/poly, not cotton"],
    ["Fleece / sweater (mid layer)", "Must", "₹600–1,200", "—", "Buy"],
    ["Padded / down jacket (rated −5 to −10 °C)", "Must", "₹2,500–5,000", "Indiahikes rentals ₹55–80/day (ships to you); trek operators ₹100/day; "
     "Manali / Gulmarg shops ₹150–300/day", "Rent if you'll never use it again. 10 days ≈ ₹600–1,000"],
    ["One-piece snow suit", "At snow points", "—", "Solang/Palchan, Kufri, Gulmarg, Tsomgo ₹250–500/day (often with gumboots)", "Rent on the spot only on snow days"],
    ["Gumboots / snow boots", "At snow points", "—", "₹100–200/day (Lachung ~₹100; bundled with suit at Solang ₹400–500)", "Rent on the spot"],
    ["Waterproof trekking shoes", "Must (Plans 2, 4, 5)", "₹2,000–3,500 (Decathlon MH100/MH500)", "Trek operators ₹100–150/day", "Buy if you'll trek again"],
    ["Waterproof gloves + woollen inners", "Must", "₹300–900 + ₹150", "—", "Buy"],
    ["Woollen cap / balaclava / neck gaiter", "Must", "₹200–400 each", "—", "Buy"],
    ["Woollen socks (4 pairs)", "Must", "₹400–600", "—", "Buy"],
    ["UV400 sunglasses", "Must on snow", "₹300–800", "—", "Snow glare causes snow-blindness"],
    ["Microspikes + gaiters", "Chopta, Hatu, Jalori, Gulmarg walks", "₹1,200–1,800", "Chopta/Sari/Sankri ₹150–250/day; gaiters ₹100/day", "Rent"],
    ["Trekking pole", "Treks", "₹400–700", "₹50–100/day", "Rent"],
    ["Ski kit (skis, boots, poles)", "Optional", "—", "Gulmarg ≈ ₹700/day + jacket ₹300 + trouser ₹200; Solang ski + instructor ₹1,000–1,500/hr", "Optional activity"],
    ["Cold cream, SPF 50, lip balm, hand-warmers", "Must", "₹500–700 total", "—", "Buy"],
]
GEAR_SUMMARY = ("<b>Budget for gear:</b> if you own nothing warm, expect ₹4,000–6,500 one-time purchase (thermals, fleece, gloves, cap, "
                "socks, sunglasses) + ₹800–1,500 in rentals on the trip (jacket, suit, boots, spikes). The per-plan budgets "
                "include only the <b>rental</b> part; the purchases you keep are listed separately.")

PACKING = [
    "Original photo ID (Aadhaar/DL) + 2 photocopies + <b>4 passport photos</b> (Sikkim permits, J&amp;K checks).",
    "Power bank (cold drains batteries 2× faster), offline Google Maps, cash ₹5–8k (ATMs fail in snow areas).",
    "Basic meds: Diamox (only after a doctor's advice) for Nathula / Chandrashila / Zuluk, paracetamol, ORS, cold & cough tabs, band-aids, Vaseline.",
    "Small daypack, reusable bottle, thermos (hot water in −5 °C mornings), quick-dry towel, plastic bags for wet gear.",
    "Prepaid SIMs from outside J&amp;K do not work in Kashmir. Carry at least one <b>postpaid</b> connection (Plan 3).",
]

COMMON_SAFETY = [
    "Snow and roads change by the hour. Check HP/J&amp;K/Sikkim/Uttarakhand police traffic updates and ask your homestay every evening. "
    "National emergency: <b>112</b>. HP disaster helpline: <b>1077</b>.",
    "Do not ride rented two-wheelers on fresh snow or black ice (Solang–Atal Tunnel, Narkanda, Gulmarg road, Chopta). Taxis with snow chains are safer after snowfall.",
    "Book stays for 24 Dec–1 Jan <b>in advance</b> (NYE rates in Manali/Shimla/Gulmarg/Darjeeling go 2–3× normal). Prefer free-cancellation rates.",
    "Keep 3 Jan as a pure buffer: plan to start the last long leg (hills → Delhi/airport) by 1 Jan, because snow and NYE traffic delay buses 3–8 h.",
]
