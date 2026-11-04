"""Plan 1: Standard Shimla (by Kalka toy train) + Manali, for 6 people, Airbnb stays."""
from common import PlanDoc, totals, k
import sections as X

BUDGET = [
    ("Train Hyderabad → Delhi (12723)", 800, 2100, "SL vs 3A"),
    ("Delhi day: metro pass, cloak room, Red Fort, food extras", 400, 500, ""),
    ("12311 Kalka Mail, Old Delhi → Kalka", 200, 200, "SL (short overnight run; 3A ≈ +₹400)"),
    ("Toy train Kalka → Shimla", 65, 65, "52453 2S (Shivalik Deluxe CC ≈ ₹510 if you prefer)"),
    ("Shimla taxis to Airbnb, Jakhoo ropeway, local", 300, 400, ""),
    ("Kufri–Narkanda–Hatu day (Innova ≈ ₹5,000)", 850, 850, "÷ 6"),
    ("Shimla → Manali HRTC", 550, 900, "Ordinary vs deluxe/Volvo"),
    ("Manali cabs: Solang–Atal–Sissu, Naggar–Jana–Sethan, Kasol–Bhuntar", 2250, 2250, "≈ ₹13.5k of Innova circuits ÷ 6"),
    ("3 scooties for the Manali day + fuel", 450, 450, "2 per scooty"),
    ("Bhuntar → Delhi bus", 1000, 1600, "HRTC ordinary vs Volvo"),
    ("Delhi half-day on 2 Jan (metro, Humayun's Tomb)", 300, 400, ""),
    ("Train Delhi → Hyderabad (12724)", 800, 2100, "SL vs 3A"),
    ("Airbnb: 2N Shimla + 4N Manali (incl. NYE)", 7400, 10000, "Entire 3-bedroom homes ÷ 6"),
    ("Food, 10 days", 5500, 6500, "Cook breakfast in the Airbnb"),
    ("Activities & entries (Solang ropeway/ski, Naggar, skating)", 1200, 2000, ""),
    ("Winter gear rentals", 800, 1000, ""),
    ("Buffer", 800, 1000, ""),
]


def build(path):
    lo, hi = totals(BUDGET)
    d = PlanDoc(path,
                "Plan 1 · Classic Shimla (toy train) + Manali",
                "Delhi day → overnight Kalka Mail → UNESCO toy train to Shimla, Kufri, Narkanda–Hatu Peak, Manali, Solang, Atal Tunnel–Sissu, "
                "Naggar, Jana, Sethan, Kasol–Manikaran. 6 people · Airbnb stays · 24 Dec 2026 – 3 Jan 2027",
                "#1d4ed8", "PLAN 1 · STANDARD SHIMLA–MANALI")

    d.h1("At a glance")
    d.table([
        ["Route", "Hyderabad → (12723) → Delhi day → (Kalka Mail) → Kalka → <b>toy train</b> → Shimla 2N → (HRTC) → Manali 4N → Kasol day → "
                  "(bus from Bhuntar) → Delhi → (12724) → Hyderabad"],
        ["Nights", "2 train out (24, 25) · 2 Shimla · 4 Manali · 1 bus · 1 train back"],
        ["Snow chances", "High: Hatu Peak, Solang, Atal Tunnel–Sissu, Sethan. Medium: Kufri, Narkanda. Low: Shimla town"],
        ["Crowd level", "High at Mall Road, Kufri, Solang, Atal Tunnel on 25 Dec and 31 Dec–1 Jan. Low at Hatu, Tani Jubbar, Jana, Sethan, Naggar"],
        ["Budget per person (6 people)", f"<b>≈ {k(lo)} shoestring</b> (SL, ordinary buses) · <b>≈ {k(hi)} recommended</b> (3A on the long trains, Volvo, better Airbnbs)"],
        ["Temperatures", "Shimla −2 to 10 °C · Manali −5 to 7 °C · Sissu/Hatu −10 to −2 °C"],
    ], [0.24, 0.76], header=False, bold_first_col=True)
    d.callout("What changed for 6 people + toy train",
              ["<b>Toy train is in:</b> instead of a Delhi→Shimla bus, you take the overnight Kalka Mail (SL ≈ ₹200) and the 05:20–06:20 toy train "
               "(2S ≈ ₹65). That's cheaper than the Volvo, and you sleep on the train instead of paying for a night.",
               "<b>The Delhi gap (07:40–21:10 on 25 Dec) is a sightseeing day</b>: Red Fort, Chandni Chowk, India Gate, Christmas at Sacred Heart.",
               "<b>Costs split 6 ways:</b> one Innova per circuit (≈ ₹750–950 each), 3-bedroom Airbnbs (≈ ₹1,000–2,300 each per night), 3 scooties."], "good")

    d.h1("Getting there and back")
    X.onward(d, (1, 2, 3, 4))
    X.kalka_toy_train(d)
    d.callout("Fast-track option (Shimla on 25 Dec evening)",
              ["Board <b>12621 Tamil Nadu Express at Kazipet 06:55</b> (Warangal 06:50, Vijayawada ~04:00) → New Delhi 06:30 → <b>12011 Kalka Shatabdi "
               "07:40</b> → Kalka 11:40 → <b>52455 Himalayan Queen 12:10</b> → Shimla ~17:20.",
               "Costs ≈ ₹1,150 pp in trains (vs ≈ ₹265) + one more Shimla Airbnb night (≈ ₹1,000–1,500 pp) + getting to Kazipet by 06:30 "
               "(night bus ≈ ₹250 or Innova ≈ ₹750 pp). It gains ~17 hours in Shimla. Only 70 min of buffer at Delhi, so book the Shatabdi after "
               "checking the train's running status (see note above)."], "info")
    X.returns(d, (1, 2, 4))
    d.h2("Hill legs")
    d.table([
        ["Leg", "Best option", "Time", "Approx cost / person"],
        ["Shimla → Manali", "HRTC from ISBT Tutikandi (06:00–09:00 departures) via Mandi–Kullu. Innova one-way ≈ ₹9,000–10,000 (÷6 ≈ ₹1,600)",
         "8–10 h", "₹550 ordinary · ₹900 deluxe/Volvo"],
        ["Bhuntar / Manali → Delhi", "HRTC ordinary/semi-deluxe or Volvo, 16:00–19:30 departures. Book Manali→Delhi with boarding point Bhuntar",
         "12–14 h", "₹950–1,100 ordinary · ₹1,600–2,000 Volvo"],
    ], [0.17, 0.5, 0.1, 0.23])
    X.vehicles(d)

    d.h1("Day-by-day itinerary")
    d.day("Day 1 · Thu 24 Dec", "Hyderabad → on the train", [
        "<b>06:00 12723 Telangana Express</b> from Hyderabad Deccan (06:25 Secunderabad, 08:05 Kazipet).",
        "Carry dinner + next-day breakfast; e-catering delivers at Nagpur, Bhopal, Jhansi.",
    ], stay="Train", cost="₹300 food")
    d.day("Day 2 · Fri 25 Dec", "Delhi sightseeing day → overnight Kalka Mail", [
        "~07:40 New Delhi → Metro Yellow Line to Chandni Chowk → leave bags at the <b>Old Delhi (Delhi Jn) cloak room</b>.",
        "<b>Red Fort</b> → <b>Jama Masjid</b> → <b>Chandni Chowk</b> lunch (Paranthe Wali Gali) → <b>Gurudwara Sis Ganj</b> → Metro to "
        "<b>Kartavya Path / India Gate</b> → <b>Agrasen ki Baoli</b> → <b>Connaught Place</b> → Christmas evening at <b>Sacred Heart Cathedral</b>.",
        "Dinner near Old Delhi, collect bags, board <b>12311 Kalka Mail ~21:10</b> (SL). Set an alarm: Kalka is the last stop, ~03:00–04:40.",
    ], stay="Train (SL)", cost="₹700 Delhi day + ₹200 train")
    d.day("Day 3 · Sat 26 Dec", "Kalka → UNESCO toy train → Shimla", [
        "Wait in the Kalka station waiting hall (1–3 h). Board <b>52451 Shivalik Deluxe 05:20–05:45</b> (CC, breakfast) or <b>52453 Express "
        "06:00–06:20</b> (2S ≈ ₹65). 96 km, 100+ tunnels, Barog station.",
        "Shimla ~10:30–11:50. Taxi/porter to the Airbnb. Afternoon: <b>The Ridge, Christ Church, Mall Road, Scandal Point, Lakkar Bazaar</b>; "
        "<b>Jakhoo Temple</b> by ropeway. Evening: Shimla Winter Carnival on the Ridge (usually 25 Dec–1 Jan); ice-skating rink if it's cold enough.",
    ], stay="Airbnb Shimla", cost="₹65–510 toy train + ₹400 local + ₹700 food")
    d.day("Day 4 · Sun 27 Dec", "Kufri → Fagu → Narkanda → Hatu Peak → Tani Jubbar", [
        "Innova for the day (≈ ₹5,000). Leave by 08:00. <b>Kufri</b> (Mahasu pony ride ₹500–800, bargain; keep it short, it's crowded).",
        "<b>Narkanda</b> ski slopes if snow has settled → <b>Hatu Peak (3,400 m)</b> wooden temple (walk the last 7 km if it's snow-bound) → "
        "<b>Tani Jubbar lake</b> (offbeat). Back in Shimla ~19:00.",
    ], stay="Airbnb Shimla", cost="₹850 cab share + ₹500 activities + ₹700 food")
    d.day("Day 5 · Mon 28 Dec", "Shimla → Manali by HRTC", [
        "Morning HRTC from Tutikandi ISBT via Sundernagar lake, Mandi, Pandoh Dam, Aut tunnel, Kullu → Manali ~17:00. Book seats the evening before.",
        "Evening: Mall Road, Manu Market, Tibetan monastery.",
    ], stay="Airbnb Old Manali", cost="₹550–900 bus + ₹700 food")
    d.day("Day 6 · Tue 29 Dec", "Solang Valley → Atal Tunnel → Sissu", [
        "Leave <b>07:00</b> in a taxi-union Innova (≈ ₹5,000–6,000 per circuit). Rent suits + gumboots at Palchan (₹300–500).",
        "Solang: ropeway (₹500–800), skiing lesson (₹1,000–1,500/hr), snow scooter (bargain). <b>Atal Tunnel (9.02 km)</b> → <b>Sissu</b> frozen "
        "waterfall and Chandra river. No permit needed for the tunnel; police stop vehicles at Solang/Dhundi after heavy snow.",
    ], stay="Airbnb Old Manali", cost="₹920 cab share + ₹1,500 activities/rent + ₹700 food")
    d.day("Day 7 · Wed 30 Dec", "Manali local by scooty + Jogini falls", [
        "3 scooties (₹500–800/day each). Hadimba Devi, Ghatotkacha shrine, Manu Temple, Old Manali cafés.",
        "Vashisht hot springs → <b>Jogini waterfall</b> trek (~2.5 km each way). Evening: Club House, Mall Road.",
    ], stay="Airbnb Old Manali", cost="₹450 scooty + ₹700 food")
    d.day("Day 8 · Thu 31 Dec", "Naggar → Jana waterfall → Sethan · NYE", [
        "Innova circuit (≈ ₹3,500): <b>Naggar Castle</b> + <b>Roerich Art Gallery</b> → <b>Jana waterfall</b> village lunch (makki-di-roti, siddu) → "
        "<b>Sethan</b> snow village and igloo cafés.",
        "NYE at the Airbnb: bonfire/BBQ (ForestBound has one), or Old Manali cafés with live music (pre-book tables).",
    ], stay="Airbnb Old Manali", cost="₹580 cab share + ₹1,000 NYE dinner")
    d.day("Day 9 · Fri 1 Jan", "Manali → Kasol, Manikaran → overnight bus from Bhuntar", [
        "Check out by 08:00 (1 Jan jams). Innova Manali → <b>Kasol</b> → <b>Manikaran Sahib</b> (hot springs, langar) → <b>Chalal</b> village walk → "
        "drop at <b>Bhuntar</b>.",
        "Overnight bus to Delhi from Bhuntar (18:00–19:30).",
    ], stay="Overnight bus", cost="₹750 cab share + ₹1,000–1,800 bus + ₹600 food")
    d.day("Day 10 · Sat 2 Jan", "Delhi half-day → train home", [
        "Arrive Majnu ka Tilla / Kashmere Gate ~06:00–08:00. Tibetan breakfast at Majnu ka Tilla → <b>Humayun's Tomb</b> → <b>Lodhi Garden</b>.",
        "<b>16:00 12724 Telangana Express</b> from New Delhi (backup: 22692 Rajdhani from Nizamuddin late evening).",
    ], stay="Train", cost="₹400 Delhi + ₹600 food")
    d.day("Day 11 · Sun 3 Jan", "Home", ["Hyderabad Deccan ~17:10."])

    X.airbnb(d, [
        ["2 (26–27 Dec)", "Shimla (Mall/Chhota Shimla side)",
         "<b>VICTORIAN VILLAS 3BHK</b>: entire unit, 3 BR, 6 guests, 4.51★ (106 reviews), the most-reviewed 3BR for 6 in Shimla",
         "<b>Jasm Homes 3BHK</b> or the 3BR <b>'Breathtaking Himalayan view'</b> apartment near Mall Road; Airbnb Shimla floor ≈ ₹949/night for small units",
         (6000, 9000)],
        ["4 (28–31 Dec)", "Old Manali",
         "<b>The ForestBound Cottage 3BHK</b> (BBQ, fireplace): 4.97★, ~70 reviews, Guest favourite, near Hadimba &amp; Old Manali cafés",
         "<b>Skye Lodges 3BR</b> (4.85★, 60) · <b>3 Bedrooms Cottage near Mall Road</b> (4.88★, 40) · cheapest: Vashisht homestays "
         "(e.g. North Himalayan Home Stay; steep last stretch)", (8000, 14000)],
    ])

    d.h1("Places covered")
    d.table([
        ["Place", "Type", "Why go", "Crowd (late Dec)"],
        ["Old Delhi, Red Fort, India Gate", "Main", "Uses the 13-hour Delhi gap", "High"],
        ["Kalka–Shimla toy train", "Main (UNESCO)", "102 tunnels, Barog, slow scenic ride", "High on 25–27 Dec"],
        ["Shimla Ridge, Mall, Christ Church, Jakhoo", "Main", "Colonial heart; Winter Carnival", "Very high"],
        ["Kufri", "Main", "Snow point", "Very high"],
        ["Narkanda + Hatu Peak, Tani Jubbar", "Offbeat", "Best snow near Shimla; quiet lake", "Low"],
        ["Solang, Atal Tunnel, Sissu", "Main", "Assured snow, Lahaul views", "Very high"],
        ["Hadimba, Old Manali, Vashisht", "Main", "Temples, cafés, hot springs", "High"],
        ["Jogini falls, Naggar, Jana, Sethan", "Offbeat", "Forest trail, old capital, village food, igloo village", "Low"],
        ["Kasol, Manikaran, Chalal", "Main + offbeat", "Parvati valley", "Medium"],
    ], [0.3, 0.15, 0.37, 0.18])

    d.h1("Bike / scooty rentals")
    d.table([
        ["Town", "Rates (per day)", "Where / how", "Notes"],
        ["Manali", "Scooty ₹500–800 · RE Classic 350 ₹1,200–1,500 · Himalayan ₹1,500–2,500", "Mall Road, Old Manali, Vashisht shops; Bike Wale "
         "Bhaiya, Riderly", "Deposit ₹1,000–2,000 + original DL. 3 scooties for 6. No riding beyond Solang on snow/ice"],
        ["Shimla", "Scooty ₹500–800", "Near ISBT / Lakkar Bazaar", "Mall Road is pedestrian; not needed here"],
        ["Kasol", "Scooty ₹600–900 · RE ₹1,200–1,600", "Kasol market", "Only if roads are dry"],
    ], [0.1, 0.3, 0.3, 0.3])

    X.gear(d, [
        ["Point", "What you can rent", "Rate"],
        ["Kufri / Narkanda stalls", "Snow suit, gumboots", "₹300–500 per set/day"],
        ["Palchan / Solang", "Suit + gumboots + gloves, ski kit", "₹300–500; ski + lesson ₹1,000–1,500"],
        ["Manali Mall Road / Old Manali", "Down jackets, boots (cheap to buy at the Tibetan market)", "₹150–300/day"],
        ["Indiahikes rentals (ships to you)", "Padded jacket (−10 °C), trek shoes", "₹55–100/day"],
    ])

    d.h1("Budget per person (6 people sharing)")
    d.budget(BUDGET, "Shoestring fits easily. Recommended is above ₹30k mainly because of 3A on the two 25-hour trains and NYE-week Manali "
                     "Airbnbs; SL on those two trains brings it to ≈ ₹29.7k.")

    d.h1("Bookings to do now (in order)")
    d.bullets([
        "<b>Today:</b> 12724 return (2 Jan) for 6 on one PNR. Then 12723 onward (24 Dec), then <b>12311 Kalka Mail (25 Dec)</b> and the "
        "<b>toy train (26 Dec)</b>. Both opened in late October, so do it now.",
        "Airbnb Manali 28 Dec–1 Jan (NYE minimum stays), then Shimla 26–28 Dec.",
        "Bhuntar/Manali → Delhi bus for 1 Jan (HRTC opens ~30 days ahead). Buy Shimla→Manali HRTC tickets the evening before.",
    ])
    d.h1("Plan B")
    d.bullets([
        "Telangana Express very late (after 19:00 in Delhi)? Still fine for the 21:10 Kalka Mail. If you miss it, take the HRTC overnight Volvo "
        "to Shimla from Kashmere Gate (≈ ₹1,000) and skip the toy train.",
        "Atal Tunnel closed after snow: Solang/Dhundi, or swap with Day 8 (Sethan).",
        "Hatu snow-bound: walk part-way, or do Chail + Kufri instead.",
        "1 Jan jams: skip Kasol and board the bus from Manali directly.",
    ])
    X.packing_and_safety(d)
    d.sources([
        "Kalka–Shimla toy train timings/fares: travelcoffee.in 2026 guide, Shimla Tourism, holidify, tusktravel, exploreindia, totaltraininfo",
        "12311 Netaji (Kalka Mail): Cleartrip, RailMitra, indiantrain, nativeplanet, totaltraininfo (Old Delhi ~21:10; Kalka 03:00–04:40, sources differ)",
        "12011/12005 Kalka Shatabdi: ixigo, Bajaj Finserv, ConfirmTkt, totaltraininfo; 12621/12625/12615 at Kazipet/Warangal/Vijayawada: ConfirmTkt, ixigo, MakeMyTrip, indiarailinfo",
        "Airbnb listings (ratings/reviews): airbnb.co.in / airbnb.com Shimla, Old Manali, Vashisht pages via search (Nov 2026)",
        "Innova/Tempo rates: Rajputana Cabs, Triveni Cabs (2026 pages); HRTC fares: mytnstc HRTC table, EaseMyTrip, trekgo",
        "Atal Tunnel/Sissu winter access: The Tribune, discoverkullumanali.in; Manali rentals & snow gear: vargiskhan, travelcoffee, Tripoto",
    ])
    d.build()
    return lo, hi
