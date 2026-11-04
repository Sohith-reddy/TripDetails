"""Plan 6 (new): Amritsar + Dalhousie–Khajjiar + Dharamshala–McLeodganj–Triund + Bir (Kangra valley), 6 people, Airbnb."""
from common import PlanDoc, totals, k
import sections as X

BUDGET = [
    ("Train Hyderabad → Delhi (12723)", 800, 2100, "SL vs 3A"),
    ("Delhi day (metro, cloak room, entries)", 400, 500, ""),
    ("Delhi → Amritsar overnight", 350, 350, "SL (3A ≈ ₹950)"),
    ("Amritsar local + Wagah border Innova", 500, 500, "≈ ₹3,000 ÷ 6"),
    ("Innova legs: Amritsar→Dalhousie, Khajjiar–Dainkund day, Dalhousie→McLeodganj, McLeodganj→Palampur→Bir", 3450, 3450, "≈ ₹20.6k ÷ 6"),
    ("Triund entry + Galu taxi", 250, 250, "₹100 forest fee + shared taxi"),
    ("Bir paragliding (optional)", 0, 2800, "₹2,500–3,000 tandem, weather permitting"),
    ("Bir / Palampur → Delhi overnight bus", 800, 1400, "HRTC ordinary vs Volvo"),
    ("Delhi half-day on 2 Jan", 300, 400, ""),
    ("Train Delhi → Hyderabad (12724)", 800, 2100, "SL vs 3A"),
    ("Airbnb: Amritsar 1N, Dalhousie 2N, McLeodganj 2N, Bir 1N (NYE)", 4800, 7350, "Entire 3BR homes ÷ 6"),
    ("Food (Golden Temple langar is free)", 5000, 5500, ""),
    ("Entries (Partition Museum, Norbulingka, Kangra Fort)", 300, 500, ""),
    ("Gear rentals (spikes for Triund)", 600, 800, ""),
    ("Buffer", 800, 1000, ""),
]


def build(path):
    lo, hi = totals(BUDGET)
    d = PlanDoc(path,
                "Plan 6 · Amritsar, Dalhousie, Dharamshala &amp; Bir",
                "Golden Temple and the Wagah retreat, Dalhousie–Khajjiar–Dainkund snow, McLeodganj and the Triund ridge, Norbulingka, Palampur tea, "
                "Baijnath, Bir (paragliding capital), plus the restored Kangra Valley toy train. 6 people · Airbnb · 24 Dec 2026 – 3 Jan 2027",
                "#9333ea", "PLAN 6 · AMRITSAR + KANGRA VALLEY")

    d.h1("At a glance")
    d.table([
        ["Route", "Hyderabad → Delhi day → overnight train → <b>Amritsar</b> 1N → <b>Dalhousie</b> 2N (Khajjiar, Kalatop, Dainkund) → <b>McLeodganj</b> 2N "
                  "(Triund) → Palampur–Baijnath → <b>Bir</b> 1N (NYE) → overnight bus → Delhi → Hyderabad"],
        ["Why this plan", "Mixes the best of Punjab and western Himachal: the Golden Temple, a border ceremony, snow at Khajjiar/Dainkund, Tibetan "
                          "McLeodganj and a ridge trek, tea gardens and paragliding. Little overlap with Plans 1–2, and less traffic than Manali at NYE."],
        ["Snow chances", "Medium–high at Dainkund and Triund. Medium at Khajjiar (late Dec). Low at Dalhousie town and Bir. None in Amritsar"],
        ["Crowd level", "High at the Golden Temple and Wagah. Medium in McLeodganj. Low at Kalatop, Dainkund, Bir"],
        ["Budget per person (6 people)", f"<b>≈ {k(lo)} shoestring</b> · <b>≈ {k(hi)} recommended</b> (incl. paragliding)"],
        ["Temperatures", "Amritsar 4–18 °C (dense fog mornings) · Dalhousie −2 to 9 °C · McLeodganj 1–12 °C · Triund −5 to 4 °C"],
    ], [0.22, 0.78], header=False, bold_first_col=True)

    d.h1("Getting there and back")
    X.onward(d, (1, 2, 3, 4))
    X.delhi_day(d)
    d.h2("Intermediate legs (cheapest that connect)")
    d.table([
        ["Leg", "Option", "Time", "Approx cost / person"],
        ["Delhi → Amritsar (25 Dec night)", "Overnight sleeper trains from New/Old Delhi or Nizamuddin (e.g. 12903 Golden Temple Mail calls at Nizamuddin; "
         "several others leave ~21:00–23:30 and reach ~05:00–07:30). Pick one that leaves after 20:30", "7–9 h", "SL ≈ ₹350 · 3A ≈ ₹950"],
        ["Amritsar → Dalhousie", "Innova (≈ ₹6,000 one-way, ~5 h via Pathankot) or bus to Pathankot + HRTC to Dalhousie (cheaper, ~7 h)", "5–7 h",
         "≈ ₹1,000 (Innova ÷ 6) or ₹350 by bus"],
        ["Dalhousie → McLeodganj", "Innova (~120 km)", "4 h", "≈ ₹900"],
        ["McLeodganj → Bir", "Innova via Norbulingka, Palampur, Baijnath", "3–4 h with stops", "≈ ₹850"],
        ["Bir / Palampur → Delhi (1 Jan night)", "HRTC ordinary/Volvo from Baijnath/Palampur (also private Volvos from Bir)", "11–13 h", "₹800–1,400"],
        ["<b>Kangra Valley toy train</b> (optional)", "Narrow-gauge Pathankot–Joginder Nagar line, <b>restored June 2026</b>. Ride a short scenic stretch, "
         "e.g. Kangra/Nagrota → Paprola (Baijnath) on Day 8, with the Innova meeting you", "2–3 h segment", "₹20–50 (unreserved)"],
    ], [0.2, 0.48, 0.12, 0.2])
    d.small("Kangra toy train timetable could not be confirmed online. Check at Kangra / Nagrota station or NTES (search 'Pathankot Joginder Nagar') a day before.")
    X.returns(d, (1, 2, 4))
    X.vehicles(d)

    d.h1("Day-by-day itinerary")
    d.day("Day 1 · Thu 24 Dec", "Hyderabad → Delhi", ["<b>06:00 12723 Telangana Express</b> (or 12621 from Kazipet 06:55 → New Delhi 06:30)."],
          stay="Train", cost="₹300 food")
    d.day("Day 2 · Fri 25 Dec", "Delhi day → overnight to Amritsar", ["Old Delhi circuit + India Gate + Sacred Heart (Christmas). Night train to Amritsar (SL)."],
          stay="Train", cost="₹700 Delhi + ₹350 train")
    d.day("Day 3 · Sat 26 Dec", "Golden Temple · Jallianwala Bagh · Wagah retreat", [
        "Golden Temple in the early morning (quietest) → langar → <b>Jallianwala Bagh</b> → <b>Partition Museum</b> (Town Hall) → heritage street.",
        "<b>Attari–Wagah Beating Retreat</b>: in winter it starts around 16:15–16:30; reach by 14:30 with ID. Innova return ≈ ₹2,500.",
        "Night: Golden Temple lit up; dinner at Kesar da Dhaba / Bharawan da Dhaba; Amritsari kulcha for breakfast.",
    ], stay="Airbnb Amritsar", cost="₹500 cab share + ₹700 food")
    d.day("Day 4 · Sun 27 Dec", "Amritsar → Dalhousie", [
        "Innova via Pathankot (~5 h). Afternoon: Gandhi Chowk, Mall Road, St John's Church, Subhash Baoli, Panchpula.",
    ], stay="Airbnb Dalhousie", cost="₹1,000 Innova share + ₹700 food")
    d.day("Day 5 · Mon 28 Dec", "Khajjiar · Kalatop · Dainkund (snow day)", [
        "<b>Khajjiar</b> (22 km): deodar-ringed meadow with a lake, snow-covered in some late-December years. <b>Kalatop</b> sanctuary forest walk.",
        "<b>Dainkund peak / Pohlani Mata temple</b> (2,755 m, highest point around Dalhousie and the snowiest): 30–45 min walk from the road.",
        "Avoid driving the Khajjiar/Dainkund roads after dark (black ice).",
    ], stay="Airbnb Dalhousie", cost="₹670 Innova share + ₹700 food")
    d.day("Day 6 · Tue 29 Dec", "Dalhousie → McLeodganj", [
        "~4 h drive. <b>Tsuglagkhang</b> (Dalai Lama temple complex) and the Tibet Museum → <b>Bhagsunag falls</b> → <b>Dharamkot</b> cafés.",
        "Rent microspikes in McLeodganj/Dharamkot for tomorrow (₹150–250).",
    ], stay="Airbnb McLeodganj / Dharamkot", cost="₹900 Innova share + ₹700 food")
    d.day("Day 7 · Wed 30 Dec", "Triund ridge day hike", [
        "Start 07:30 from <b>Galu Devi temple</b> (forest check post; ₹100 per person per day). ~7–9 km one way, 3–4 h up. Dhauladhar wall in snow.",
        "In heavy snow the trail closes for some weeks; Kangra police have at times required prior intimation for Triund. Check at the check post. "
        "Day hike only (camping rules keep changing). Turn back by 13:00.",
    ], stay="Airbnb McLeodganj", cost="₹250 entry/taxi + ₹700 food")
    d.day("Day 8 · Thu 31 Dec", "Norbulingka → Palampur tea → Baijnath → Bir (NYE)", [
        "<b>Norbulingka Institute</b> (Tibetan arts) → <b>Kangra Fort</b> (optional) → <b>Palampur</b> tea gardens (Wah / Mann tea estates) → 9th-century "
        "<b>Baijnath temple</b> → <b>Bir</b>. Option: ride the Kangra toy train for one stretch.",
        "Bir: Tibetan colony, Chokling monastery, sunset at the landing site. NYE bonfire at the Airbnb.",
    ], stay="Airbnb Bir", cost="₹850 Innova share + ₹300 entries + ₹900 food/NYE")
    d.day("Day 9 · Fri 1 Jan", "Bir paragliding → overnight bus to Delhi", [
        "<b>Tandem paragliding</b> from Billing (₹2,500–3,000, 15–20 min). Winter flights depend on the Billing road being clear of snow, so "
        "book with a registered operator and check that morning.",
        "Evening HRTC/private bus from Bir/Baijnath/Palampur to Delhi.",
    ], stay="Overnight bus", cost="₹2,800 (optional) + ₹800–1,400 bus + ₹600 food")
    d.day("Day 10 · Sat 2 Jan", "Delhi → Hyderabad", ["Humayun's Tomb / Lodhi Garden → <b>16:00 12724</b>."], stay="Train", cost="₹400 + ₹600 food")
    d.day("Day 11 · Sun 3 Jan", "Home", ["Hyderabad ~17:10."])

    X.airbnb(d, [
        ["1 (26 Dec)", "Amritsar", "<b>Cozy Condo 3BHK, 2 km from Golden Temple</b>: 4.99★ (89) · <b>Guest-fav 3BHK FamilyVilla</b> 4.97★ (60)",
         "<b>Cozy 3 bedroom Apt</b> near Golden Temple (4.5★, 28)", (4000, 6500)],
        ["2 (27–28 Dec)", "Dalhousie", "<b>Dalhousie Cottage, a 150-year-old British bungalow</b>: 2 BR, 6 guests, 4.92★ (25); the listing label says "
         "Nainital, so confirm the location · <b>The Garden Cottage, Panoramic Mountain Views</b> (sleeps 8, 4.58★, 40)",
         "<b>Birdwood Cottages</b> guest-house rooms (book 3)", (5000, 8000)],
        ["2 (29–30 Dec)", "McLeodganj / Dharamkot", "<b>Attic House with a Mountain View</b> (3 bed / 6 ppl): 4.77★ (125) · <b>Earthbound Homes Plus 3BHK</b> ~4.9★",
         "<b>The Bougainvillea</b> entire floor, 3 BR / 6 (4.67★, 6) · <b>Just Homely 3BHK</b>, Dharamshala", (5000, 8000)],
        ["1 (31 Dec)", "Bir", "<b>Workation-Bir-Billing</b> house: 4 rooms with attached baths, 6–8 guests · <b>Home in Bir</b>, independent 3BHK (6)",
         "Private rooms in Bir hostels (Tibetan colony side)", (4000, 7000)],
    ])

    d.h1("Places covered")
    d.table([
        ["Place", "Type", "Why"],
        ["Golden Temple, Jallianwala Bagh, Partition Museum", "Main", "Punjab's heart; free langar"],
        ["Attari–Wagah Beating Retreat", "Main", "Border ceremony"],
        ["Dalhousie, Khajjiar", "Main", "Colonial hill town, 'mini Switzerland' meadow"],
        ["Kalatop, Dainkund", "Offbeat", "Forest sanctuary, snowiest viewpoint"],
        ["McLeodganj, Tsuglagkhang, Bhagsu", "Main", "Tibetan exile capital"],
        ["Dharamkot, Triund ridge", "Semi-offbeat", "Cafés, ridge facing the Dhauladhar"],
        ["Norbulingka, Palampur tea, Baijnath", "Offbeat", "Tibetan crafts, tea slopes, 9th-c. temple"],
        ["Kangra Valley toy train", "Offbeat", "Restored narrow-gauge line (2026)"],
        ["Bir–Billing", "Semi-offbeat", "Paragliding, monasteries"],
    ], [0.42, 0.18, 0.4])

    d.h1("Bike / scooty rentals")
    d.table([
        ["Where", "Rates", "Notes"],
        ["McLeodganj / Dharamshala", "Scooty ₹500–800 · RE ₹1,200–1,800", "Steep, narrow lanes; fine for Naddi / Bhagsu on dry days"],
        ["Bir", "Scooty ₹500–800", "Handy for Bir colony and Baijnath. Billing road is steep: take the operator jeep"],
        ["Amritsar", "Scooty ₹400–600", "City only. Wagah is easier by Innova"],
    ], [0.2, 0.32, 0.48])

    X.gear(d, [
        ["Point", "What you can rent", "Rate"],
        ["McLeodganj / Dharamkot / Galu", "Microspikes, gaiters, poles, jackets", "₹100–250 per item/day"],
        ["Khajjiar / Dainkund stalls", "Gumboots, snow suits (on snow days)", "₹200–400"],
        ["Bir operators", "Jackets for the flight (usually included)", "Included"],
        ["Indiahikes rentals (online)", "Padded jacket, trek shoes", "₹55–150/day"],
    ])

    d.h1("Budget per person (6 people sharing)")
    d.budget(BUDGET, "Fits ₹25–30k even with paragliding and 3A on the long trains.")

    d.h1("Bookings to do now")
    d.bullets([
        "12724 return (2 Jan) → 12723 onward (24 Dec) → Delhi → Amritsar overnight (25 Dec).",
        "Airbnb Bir (31 Dec) and McLeodganj first, then Dalhousie and Amritsar.",
        "Innova for the 4 Himachal legs from one Pathankot/Dharamshala operator (fixed price in writing). Bir → Delhi bus for 1 Jan.",
        "Paragliding with a registered Bir operator (pay on the day only if they fly).",
    ])
    d.h1("Plan B")
    d.bullets([
        "Dense fog in Amritsar (common late Dec) delays trains. If the Delhi–Amritsar train is very late, keep Wagah and do the Golden Temple at night.",
        "Khajjiar/Dainkund roads iced: go to Chamera lake (lower) or stay in Dalhousie town and walk Kalatop.",
        "Triund closed: Naddi viewpoint + Dal lake (McLeod) + Gallu temple walk, or the Bhagsu–Shiva café trail.",
        "No paragliding (snow/wind): Barot valley day trip from Bir (offbeat) or Sherabling monastery.",
    ])
    X.packing_and_safety(d)
    d.sources([
        "Triund fee (₹100) and rules: The Tribune (fee cut), thetravellertrails (Jan 2026), Curly Tales (Kangra trekking rules), vargiskhan (camping)",
        "Bir paragliding prices & winter flying: trekgo, Thrillophilia, WanderOn, Outlook Traveller",
        "Kangra Valley toy train restored (June 2026): Outlook Traveller, Curly Tales, Keekli, The Tribune",
        "Khajjiar/Dalhousie snow & Dainkund: TravelTriangle, JustWravel, The Hosteller; Amritsar–Dalhousie taxi: cabbazar, oneway.cab, exploreindia",
        "Airbnb listings: airbnb.com/.co.in Amritsar, Dalhousie, McLeod Ganj, Dharamshala, Bir pages via search (Nov 2026)",
        "Golden Temple Mail 12903 route: Wikipedia mirror, totaltraininfo (Delhi times not confirmed)",
    ])
    d.build()
    return lo, hi
