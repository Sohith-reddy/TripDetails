"""Plan 1: Standard Shimla + Manali with nearby offbeat add-ons."""
from common import PlanDoc
import sections as X


def build(path):
    d = PlanDoc(path,
                "Plan 1 · Classic Shimla + Manali",
                "The standard circuit done well: Shimla, Kufri, Narkanda–Hatu Peak, Manali, Solang, Atal Tunnel–Sissu, "
                "Naggar, Jana, Sethan, Kasol–Manikaran. 24 Dec 2026 – 3 Jan 2027 · Hyderabad round trip by train",
                "#1d4ed8", "PLAN 1 · STANDARD SHIMLA–MANALI")

    d.h1("At a glance")
    d.table([
        ["Route", "Hyderabad → (train) → Delhi → (HRTC Volvo) → Shimla 3N → (bus) → Manali 4N → Kasol/Manikaran day → "
                  "(Volvo from Bhuntar) → Delhi → (train) → Hyderabad"],
        ["Nights", "2 on train out · 3 Shimla · 4 Manali · 1 Volvo · 1 train back"],
        ["Snow chances", "High at Hatu Peak, Solang, Atal Tunnel–Sissu and Sethan. Medium at Kufri and Narkanda. Low in Shimla town (some years)"],
        ["Crowd level", "High at Mall Road, Kufri, Solang and Atal Tunnel on 25 Dec and 31 Dec–1 Jan. Low at Hatu, Tani Jubbar, Jana, Sethan, Naggar"],
        ["Difficulty", "Easy. No trekking needed (Jogini falls and Hatu walk are optional)"],
        ["Budget (per person, group of 4)", "≈ ₹24.6k shoestring (SL + hostels) · ≈ ₹30.8k recommended (3A + budget hotels)"],
        ["Temperatures", "Shimla −2 to 10 °C · Manali −5 to 7 °C · Sissu/Hatu −10 to −2 °C"],
    ], [0.24, 0.76], header=False, bold_first_col=True)

    d.callout("Why this works with your dates",
              ["24 Dec morning train → Delhi on 25 Dec morning → Shimla the same evening (Christmas on the Ridge). "
               "You leave the hills on 1 Jan and Delhi on 2 Jan, so 3 Jan is a buffer.",
               "Offbeat add-ons sit next to the main sights: Hatu Peak + Tani Jubbar (beyond Kufri), Jana waterfall + Sethan (beyond Naggar), "
               "Jogini falls (beyond Vashisht), Chalal/Tosh (beyond Kasol)."], "good")

    d.h1("Getting there and back")
    X.delhi_trains(d)
    d.h2("Delhi ↔ Shimla ↔ Manali connections")
    d.table([
        ["Leg", "Best option", "Time", "Approx cost / person", "Book on"],
        ["Delhi → Shimla", "HRTC Himsuta AC Volvo from ISBT Kashmere Gate (departures around 06:45, 08:00, 09:25, 11:55, 21:00). "
         "From New Delhi station take the Metro Yellow Line to Kashmere Gate (2 stops, ~₹30)", "8–9.5 h", "₹980–1,100",
         "online.hrtchp.com, redBus, AbhiBus"],
        ["Alt: Delhi → Kalka → Shimla (toy train)", "14095 Himalayan Queen (Delhi Sarai Rohilla 05:35 → Kalka 11:10) + 52455 toy train "
         "(Kalka 12:10 → Shimla ~17:20). Only works if you're in Delhi the night before", "~12 h", "Train ₹150–500 + toy train ₹400–550",
         "IRCTC"],
        ["Shimla → Manali", "HRTC from ISBT Tutikandi, Shimla, via Mandi–Kullu (morning departures 06:00–09:00)", "8–10 h",
         "₹550–650 (ordinary/deluxe) · Volvo ~₹900 if running · private cab ₹6,500–8,000 per car", "HRTC counter / online"],
        ["Manali / Bhuntar → Delhi", "HRTC or private Volvo, evening departures 16:00–19:00, reaches Kashmere Gate / Majnu ka Tilla 06:00–08:00",
         "12–14 h", "₹1,600–2,000 (HRTC ~₹1,670; private NYE week ₹1,800–3,000)", "HRTC / redBus. Choose boarding point Bhuntar if coming from Kasol"],
    ], [0.15, 0.4, 0.09, 0.2, 0.16])
    X.flights(d, (1, 2))
    d.callout("Fast alternative (+1 day in the hills, +₹8–12k)",
              "Fly Hyderabad → Chandigarh on 24 Dec morning (IndiGo, ~2.5 h), then HRTC Volvo / taxi Chandigarh → Shimla (3–4 h, Volvo ₹500–650, "
              "taxi ₹3,000–3,500). You sleep in Shimla on 24 Dec and gain a day for Chail (offbeat palace town + world's highest cricket ground) or "
              "Tattapani hot springs. Fly Delhi → Hyderabad on 2 Jan evening if you want to skip the 25 h train ride back.")

    d.h1("Day-by-day itinerary")
    d.day("Day 1 · Thu 24 Dec", "Hyderabad → on the train", [
        "<b>06:00</b> 12723 Telangana Express from Hyderabad Deccan (or 06:25 Secunderabad). Alternative: <b>07:10 22691 Rajdhani</b> from "
        "Secunderabad (reaches Nizamuddin 05:30, so you can take the 06:45/08:00 Volvo and reach Shimla by afternoon).",
        "Carry dinner and next-day breakfast; e-catering (IRCTC eCatering / RailRestro) delivers at Nagpur, Bhopal and Jhansi.",
        "Keep winter layers in the top bag. North India mornings are 5–8 °C and foggy, and fog can delay trains 1–4 h.",
    ], stay="Train (3A/SL)", cost="₹300 food")
    d.day("Day 2 · Fri 25 Dec", "Delhi → Shimla (Christmas on the Ridge)", [
        "~07:40 New Delhi → Metro Yellow Line to Kashmere Gate ISBT → <b>09:25 HRTC Volvo</b> (fallback 11:55) → Shimla ~18:30 "
        "(Old Bus Stand / Tutikandi ISBT, then a local bus or taxi ₹300–400 to Mall Road). <b>Book the bus seat in advance for 25 Dec.</b>",
        "Evening: Christ Church lit up for Christmas, the Ridge, Scandal Point, Mall Road. The Shimla Winter Carnival usually runs on the "
        "Ridge from around 25 Dec to 1 Jan.",
    ], stay="Budget hotel near Mall / Lakkar Bazaar (₹1,800–2,800 per room)", cost="₹1,000 bus + ₹600 food")
    d.day("Day 3 · Sat 26 Dec", "Shimla sightseeing + offbeat walks", [
        "Jakhoo Temple (ropeway or a steep 30-min walk; watch out for monkeys, keep specs and phones inside), Christ Church, Gaiety Theatre, "
        "Lakkar Bazaar woodcraft.",
        "<b>Shimla Ice Skating Rink</b> (one of Asia's oldest natural rinks) usually opens late Dec–Jan if nights are cold enough. "
        "Morning and evening sessions, skates on hire.",
        "Afternoon: Indian Institute of Advanced Study (Viceregal Lodge, guided tour) → walk the quiet Summer Hill / Annandale side.",
        "Optional offbeat: Tara Devi temple (sunset view) or the Glen forest walk.",
    ], stay="Same hotel", cost="₹500 entries + ₹700 food + ₹200 local")
    d.day("Day 4 · Sun 27 Dec", "Kufri → Fagu → Narkanda → Hatu Peak → Tani Jubbar (snow day)", [
        "Hire a cab for the day (₹3,500–4,500 per car). Leave by 08:00 to beat Kufri traffic.",
        "<b>Kufri</b> (main sight): Mahasu Peak pony ride (₹500–800, bargain), snow-point stalls. It's crowded, so keep it short.",
        "<b>Narkanda (2,708 m)</b>: HPTDC ski slopes if snow has settled. <b>Hatu Peak (3,400 m)</b>: wooden Hatu Mata temple, 360° "
        "Himalayan view. If the last 7 km is snow-bound, walk it (2–2.5 h up) or turn back.",
        "<b>Tani Jubbar lake</b> (offbeat, 8 km from Narkanda): quiet lake ringed by deodars. Back in Shimla by 19:00.",
        "Rent a snow suit + gumboots at Kufri/Narkanda stalls only if there's fresh snow (₹300–500).",
    ], stay="Same hotel", cost="₹1,000 cab share + ₹500 activities + ₹700 food")
    d.day("Day 5 · Mon 28 Dec", "Shimla → Manali by HRTC", [
        "Early HRTC from Tutikandi ISBT (06:00–08:00) via Bilaspur → Sundernagar lake → Mandi → Pandoh Dam → Aut Tunnel → Kullu → Manali (~17:00).",
        "Sit on the right side after Mandi for the Beas gorge. A shared private cab is faster (7–8 h) at ₹6,500–8,000 per car.",
        "Evening: Mall Road, Manu Market momos, Tibetan Monastery.",
    ], stay="Old Manali / Vashisht guesthouse (₹2,000–3,500/room NYE week) or hostel dorm ₹700–1,500", cost="₹600 bus + ₹700 food")
    d.day("Day 6 · Tue 29 Dec", "Solang Valley → Atal Tunnel → Sissu (Lahaul)", [
        "Leave by <b>07:00</b>. Holiday queues to the tunnel build up from 09:00. Local taxi union rate for Solang + Atal Tunnel + Sissu: "
        "≈ ₹3,500–4,500 per car (more for Innova/after fresh snow). Self-drive two-wheelers aren't safe on icy stretches.",
        "Rent suit + gumboots at Palchan/Solang (₹300–500). Solang: ropeway (₹500–800), skiing lesson (₹1,000–1,500/hr), snow scooter / ATV "
        "(₹1,000–2,000, bargain hard). Paragliding depends on weather.",
        "<b>Atal Tunnel (9.02 km)</b> → <b>Sissu</b>: frozen waterfall, Chandra river, Lahaul snowscape. No permit needed for the tunnel. Police "
        "may stop vehicles at Solang/Dhundi after heavy snow, and then Solang is the snow point.",
    ], stay="Same", cost="₹1,125 cab share + ₹1,500 activities/rent + ₹700 food")
    d.day("Day 7 · Wed 30 Dec", "Manali local by scooty + Jogini falls (offbeat)", [
        "Rent a scooty (₹500–800/day + ₹1,000–2,000 deposit; Old Manali / Mall Road shops). Ride only on cleared roads.",
        "Hadimba Devi temple & Dhungri forest → Ghatotkacha shrine → Manu Temple → Old Manali cafés.",
        "Vashisht: hot-spring baths & temple → <b>Jogini waterfall</b> trek (~2.5 km each way from Vashisht, 2–3 h return).",
        "Evening: Club House, Mall Road shopping (Kullu shawls, caps).",
    ], stay="Same", cost="₹350 scooty share + ₹200 fuel + ₹800 food")
    d.day("Day 8 · Thu 31 Dec", "Naggar → Jana waterfall → Sethan · New Year's Eve", [
        "Cab circuit (₹2,500–3,000 per car): <b>Naggar Castle</b> (1460s wood-and-stone castle, small entry fee) + <b>Roerich Art Gallery</b>.",
        "<b>Jana waterfall</b> (offbeat): lunch of makki-di-roti, sarson-da-saag and siddu at the village dhabas.",
        "<b>Sethan</b> (12 km above Prini): quiet snow village with igloo cafés and a short snow walk on the Hampta trail. Far fewer people than Solang.",
        "NYE in Old Manali (cafés with live music, dinner ₹600–1,200) or a bonfire at your guesthouse. Book dinner tables early.",
    ], stay="Same", cost="₹700 cab share + ₹1,200 NYE dinner")
    d.day("Day 9 · Fri 1 Jan", "Manali → Kasol, Manikaran → overnight Volvo to Delhi", [
        "Check out by 08:00. 1 Jan traffic down to Kullu is heavy. Cab / local bus to Bhuntar → <b>Kasol</b> (Parvati valley, 32 km).",
        "<b>Manikaran Sahib</b>: hot springs, free langar. <b>Chalal</b> village walk (30 min along the Parvati). Tosh adds ~3 h, so only if time allows.",
        "Board the evening <b>Volvo to Delhi from Bhuntar</b> (book Manali→Delhi with boarding point Bhuntar/Kullu, 18:00–19:30).",
    ], stay="Overnight Volvo", cost="₹875 cab share + ₹1,800 Volvo + ₹600 food")
    d.day("Day 10 · Sat 2 Jan", "Delhi → train home", [
        "Reach Majnu ka Tilla / Kashmere Gate ~06:00–08:00. Freshen up (station retiring room, or a Paharganj day room ₹800–1,200 shared).",
        "Optional: Connaught Place, India Gate, or Humayun's Tomb if leaving from Nizamuddin.",
        "<b>16:00 12724 Telangana Express</b> from New Delhi (backup: 22692 Rajdhani from Nizamuddin late evening).",
    ], stay="Train", cost="₹300 room share + ₹600 food")
    d.day("Day 11 · Sun 3 Jan", "Home", ["Reach Hyderabad Deccan ~17:10 (Rajdhani: Secunderabad 17:10)."])

    d.h1("Places covered")
    d.table([
        ["Place", "Type", "Why go", "Crowd (late Dec)"],
        ["Shimla Ridge, Mall, Christ Church, Jakhoo", "Main", "Colonial heart of Shimla; Christmas lights", "Very high"],
        ["Kufri", "Main", "Snow point, pony rides", "Very high"],
        ["Narkanda + Hatu Peak", "Offbeat", "Best snow near Shimla, 3,400 m temple top", "Low–medium"],
        ["Tani Jubbar lake", "Offbeat", "Quiet lake in a deodar bowl", "Low"],
        ["Ice skating rink, Shimla", "Seasonal", "Natural ice; only on cold nights", "Medium"],
        ["Solang, Atal Tunnel, Sissu", "Main", "Assured snow and Lahaul views", "Very high"],
        ["Hadimba, Old Manali, Vashisht", "Main", "Temples, cafés, hot springs", "High"],
        ["Jogini falls", "Offbeat", "Short forest trek to a frozen-ish fall", "Low"],
        ["Naggar Castle, Roerich gallery", "Semi-offbeat", "Old capital of Kullu, art", "Low"],
        ["Jana waterfall, Sethan", "Offbeat", "Village food; igloo snow village", "Low"],
        ["Kasol, Manikaran, Chalal (Tosh optional)", "Main + offbeat", "Parvati valley, hot springs, langar", "Medium"],
    ], [0.3, 0.13, 0.39, 0.18])

    d.h1("Bike / scooty rentals on this route")
    d.table([
        ["Town", "Rates (per day)", "Where / how", "Notes"],
        ["Manali", "Scooty ₹500–800 · RE Classic 350 ₹1,200–1,500 · Himalayan ₹1,500–2,500", "Shops on Mall Road, Old Manali, Vashisht; "
         "online: Bike Wale Bhaiya, Riderly, local WhatsApp rentals", "Deposit ₹1,000–2,000 + original DL. No riding beyond Solang on snow/ice. "
         "Most rentals ban taking bikes over Atal Tunnel in winter"],
        ["Shimla", "Scooty ₹500–800 · 150–200 cc ₹900–1,500", "Near Shimla ISBT / Lakkar Bazaar", "Mall Road is pedestrian. Use the bike for Kufri/Chail only on clear days"],
        ["Kasol", "Scooty ₹600–900 · RE ₹1,200–1,600", "Kasol main market", "Handy for Manikaran–Barshaini (Tosh) if roads are dry"],
    ], [0.1, 0.3, 0.3, 0.3])

    X.gear(d, [
        ["Point", "What you can rent", "Rate"],
        ["Kufri / Narkanda stalls", "Snow suit, gumboots", "₹300–500 per set/day"],
        ["Palchan / Solang (before Atal Tunnel)", "One-piece suit + gumboots + gloves, ski kit", "₹300–500 suit+boots; ski kit + lesson ₹1,000–1,500"],
        ["Manali Mall Road / Old Manali", "Down jackets, boots (also cheap to buy at the Tibetan market)", "₹150–300/day"],
        ["Indiahikes rentals (online, ships to you)", "Padded jacket (−10 °C), trek shoes, poles", "₹55–100/day"],
    ])

    d.h1("Budget (per person, 4 people sharing rooms and cabs)")
    d.budget([
        ("Train Hyderabad → Delhi", 800, 2100, "SL vs 3A, Telangana Exp"),
        ("Train Delhi → Hyderabad", 800, 2100, "SL vs 3A"),
        ("Delhi → Shimla HRTC Volvo", 1000, 1000, "Book early for 25 Dec"),
        ("Shimla → Manali HRTC", 600, 600, "Deluxe/ordinary"),
        ("Bhuntar/Manali → Delhi Volvo", 1600, 1800, "NYE-week fares"),
        ("Metro, autos, local buses", 400, 500, ""),
        ("Sightseeing cabs (Narkanda day, Solang–Sissu, Naggar–Sethan, Kasol)", 3600, 3600, "₹14.5k of cabs ÷ 4"),
        ("Scooty day (2 per scooty) + fuel", 450, 550, ""),
        ("Stays: 3N Shimla + 4N Manali", 6000, 8000, "Hostel dorms vs budget hotel rooms (2/room)"),
        ("Food, 10 days (incl. train food)", 6000, 6500, "₹600–650/day"),
        ("Activities & entry tickets", 1500, 2000, "Solang ropeway/skiing, Naggar, Jakhoo, skating"),
        ("Winter gear rentals", 800, 1000, "Suit, boots, jacket"),
        ("Buffer (tips, delays, NYE)", 1000, 1000, ""),
    ], "Within ₹25–31k. Each extra person in the car saves ~₹700. Flying one way adds ₹5–8k.")

    d.h1("Bookings to do now (in this order)")
    d.bullets([
        "<b>Today:</b> return train for 2 Jan (12724 / 22692). The booking window opened on 3 Nov. Then the onward train for 24 Dec "
        "(12723 / 22691 / 12285), using the halt-by-halt method above if it shows WL.",
        "HRTC Volvo Delhi → Shimla for 25 Dec, and the Manali → Delhi Volvo for 1 Jan (HRTC opens about 30 days ahead; private operators earlier).",
        "Manali stay for 28 Dec – 1 Jan (NYE week sells out). Pick free cancellation.",
        "Shimla stay 25–28 Dec. Don't pre-book Shimla→Manali buses. Book the morning ticket at Tutikandi the evening before.",
    ])

    d.h1("Plan B if snow or traffic hits")
    d.bullets([
        "Atal Tunnel closed after snowfall: go to Solang/Dhundi, or swap with Day 8 (Sethan usually has snow and less crowd).",
        "Hatu road snow-bound: walk partway, or switch to Chail + Kufri. Narkanda town itself usually stays reachable.",
        "Train reaches Delhi late (fog): take the 11:55 Volvo, or the overnight 21:00 Volvo and sleep on the bus. Shift Shimla sightseeing to Day 3.",
        "1 Jan jams near Manali: skip Kasol and board the Volvo from Manali directly (16:00–17:00).",
    ])
    X.packing_and_safety(d)

    d.sources([
        "Train timings/days: Wikipedia (Telangana Exp, Duronto, Rajdhani pages), ConfirmTkt, totaltraininfo, ixigo, RailMitra, Trainman, gettraininfo (Nov 2026 search)",
        "IRCTC 60-day advance reservation rule (effective 1 Nov 2024): Business Today, India TV, Upstox; Aadhaar-verified booking updates: india.com, Patrika",
        "HRTC Volvo fares/timings: mytnstc.com HRTC table, EaseMyTrip, abhibus, trekgo Delhi–Shimla guide, himachal.exploreindia.in",
        "Kalka–Shimla toy train & Himalayan Queen: holidify, totaltraininfo, ixigo, Wikipedia",
        "Atal Tunnel/Sissu winter access & NYE traffic: The Tribune (Himachal), discoverkullumanali.in highway status 2026",
        "Manali rentals & snow gear: vargiskhan.com, travelcoffee.in, discoverwithdheeraj.com, Tripoto traveller notes, Thrillophilia",
        "Narkanda/Hatu offbeat notes: indianholiday.com, travelcoffee.in, Culture Trip offbeat Himachal",
        "Shimla bike rental: bikewalebhaiya.com 2025 Shimla guide, Riderly listings",
        "Flights HYD–DEL/IXC: MakeMyTrip, Goibibo, ixigo, HappyFares, Skyscanner route pages",
    ])
    d.build()
