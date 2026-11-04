"""Plan 8 (international): Nepal overland: Hyderabad→Raxaul train, Kathmandu, Bhaktapur, Patan, Bandipur, Pokhara (NYE street festival)."""
from common import PlanDoc, totals, k
import sections as X

BUDGET = [
    ("17005 Hyderabad → Raxaul (Thu 23:10)", 870, 2300, "SL vs 3A"),
    ("Raxaul → Birgunj border rickshaws", 100, 100, ""),
    ("Birgunj night (hotel, 3 rooms)", 600, 900, "No real Airbnb supply"),
    ("Birgunj → Kathmandu", 500, 1700, "Day bus vs hired Hiace for 6"),
    ("Kathmandu taxis, 2 days (2 cabs)", 800, 1000, ""),
    ("Entry tickets at SAARC rates (Durbar Squares, Swayambhu, Boudha)", 700, 900, ""),
    ("Kathmandu → Dumre (tourist bus) + jeep to Bandipur", 600, 600, ""),
    ("Bandipur → Pokhara bus", 250, 250, ""),
    ("Pokhara: boat, Sarangkot sunrise taxi, local", 600, 800, ""),
    ("Pokhara → Birgunj bus", 700, 1000, "Local vs tourist/AC"),
    ("Raxaul → Patna bus", 450, 600, ""),
    ("Patna night before the train", 700, 1000, "Airbnb/hotel near Danapur"),
    ("12792 Danapur → Secunderabad (12:15)", 840, 2200, "SL vs 3A"),
    ("Airbnb Nepal: Kathmandu 2N, Bandipur 1N, Pokhara 2N (NYE)", 4000, 6400, "Entire 3BR apartments ÷ 6"),
    ("Food, 10 days (incl. 4 train days)", 6000, 7000, "Dal bhat sets are cheap and filling"),
    ("Nepali SIM / eSIM, exchange margin", 300, 400, ""),
    ("Buffer", 800, 1000, ""),
]


def build(path):
    lo, hi = totals(BUDGET)
    d = PlanDoc(path,
                "Plan 8 · Nepal Overland (international, fits the budget)",
                "Weekly Hyderabad–Raxaul train on 24 Dec (Thursday) → Kathmandu's three Durbar Squares, Pashupatinath, Boudha → Bandipur hill town → "
                "Pokhara for the New Year street festival and Sarangkot sunrise → back via Patna. 6 people · no visa",
                "#b91c1c", "PLAN 8 · NEPAL (INTERNATIONAL)")

    d.h1("At a glance")
    d.table([
        ["Route", "Hyderabad → (17005, 42 h) → Raxaul → walk into <b>Birgunj</b> 1N → <b>Kathmandu</b> 2N → <b>Bandipur</b> 1N → <b>Pokhara</b> 2N (NYE) → "
                  "Birgunj → Raxaul → Patna 1N → (12792) → Secunderabad 3 Jan night"],
        ["Why Nepal", "The only international trip that fits ₹25–30k for these dates. No visa, no flights (the weekly train leaves exactly on "
                      "Thursday 24 Dec), and INR is widely accepted. Himalayan views (Annapurna, Machhapuchhre, Manaslu) and the Pokhara Street "
                      "Festival (usually 28 Dec–1 Jan)."],
        ["Snow", "No snow in Kathmandu/Pokhara (2–20 °C). Big snow-peak views, not snow play. Pick Plans 1–7 if you want to walk in snow"],
        ["Documents", "<b>Passport or voter ID</b> for every adult (Aadhaar is generally not accepted at the border). Children: passport or school ID + birth certificate"],
        ["Money", "₹1 ≈ NPR 1.6. Indian ₹100 and smaller notes are accepted freely. A 2025–26 rule change allows ₹200/₹500 notes up to ₹25,000 per person "
                  "(sources differ on details), so carry mostly ₹100s and use UPI where shops accept it"],
        ["Budget per person (6 people)", f"<b>≈ {k(lo)} shoestring</b> (SL, buses) · <b>≈ {k(hi)} recommended</b> (3A, hired van for the first leg). "
                                         "Paragliding is extra (NPR 9,000–12,000 ≈ ₹5,600–7,500)"],
    ], [0.2, 0.8], header=False, bold_first_col=True)
    d.callout("Why not Bhutan, Sri Lanka, Thailand, Malaysia or Vietnam?",
              ["Bhutan: SDF ₹1,200 per person per night + HYD–Bagdogra flights (₹13–17k return) + a Bhutanese car comes to ≈ ₹40–46k. "
               "Sri Lanka, Thailand, Malaysia, Vietnam: the December return flights alone are ₹21–35k. Details are in the Overview PDF."], "info")

    d.h1("Trains (both directions)")
    d.table([
        ["Leg", "Train", "Time", "Runs", "Fare (SL · 3A)", "Notes"],
        ["<b>Out</b>", "<b>17005 Hyderabad–Raxaul Exp</b>", "Hyderabad Deccan <b>23:10 Thu 24 Dec</b> (Secunderabad 23:30) → Raxaul ~16:50–17:00 Sat 26 Dec",
         "Thu only", "≈ ₹870 · ≈ ₹2,300", "~42 h. No pantry car on some days, so carry food"],
        ["<b>Back</b>", "<b>12792 Danapur–Secunderabad SF Exp</b>", "Danapur (Patna) <b>12:15 Sat 2 Jan</b> → Secunderabad ~21:30 Sun 3 Jan", "Daily",
         "≈ ₹840 · ≈ ₹2,200", "~33 h. Home 3 Jan night"],
        ["Not usable", "17006 Raxaul–Hyderabad", "Raxaul 03:15 Sun → Hyderabad 19:40 Mon", "Sun only", "", "3 Jan departure gets you home 4 Jan"],
    ], [0.08, 0.2, 0.32, 0.09, 0.13, 0.18])
    d.small("Book 17005 today: it's weekly, so there's no second chance. Both trains are well inside the 60-day window. Fallback for the way back if 12792 "
            "is full: Patna → Hyderabad flight on 2 Jan (IndiGo direct, typically ₹5–8k), or Kathmandu → Delhi → Hyderabad flights (≈ ₹13–16k).")

    d.h2("Inside Nepal")
    d.table([
        ["Leg", "How", "Time", "Approx cost / person"],
        ["Raxaul → Birgunj", "Cycle/e-rickshaw across the open border (5 km); no immigration formalities for Indians, but carry ID", "30 min", "₹50–100"],
        ["Birgunj → Kathmandu", "Day bus (NPR ~500–900) or a hired Hiace/Scorpio for 6 (≈ NPR 15–18k)", "6–8 h", "₹400–560 bus · ≈ ₹1,700 van"],
        ["Kathmandu → Dumre → Bandipur", "Tourist bus to Pokhara from Sorhakhutte 07:00, get off at <b>Dumre</b>; jeep/taxi 8 km up (20–30 min)",
         "4–5 h", "NPR ~800–1,200 + jeep"],
        ["Bandipur → Pokhara", "Jeep to Dumre + local/tourist bus", "2.5–3 h", "NPR ~400"],
        ["Pokhara → Birgunj", "Direct day bus via Narayanghat", "7–9 h", "NPR 1,000–1,500"],
        ["Raxaul → Patna", "Bus via Motihari–Muzaffarpur", "5–6 h", "₹350–500"],
    ], [0.2, 0.48, 0.1, 0.22])

    d.h1("Day-by-day itinerary")
    d.day("Day 1 · Thu 24 Dec", "Hyderabad → on the Raxaul train", ["Day free in Hyderabad. <b>23:10 17005</b> from Hyderabad Deccan (23:30 Secunderabad)."],
          stay="Train", cost="—")
    d.day("Day 2 · Fri 25 Dec", "On the train", ["A long run through central India into Bihar. Christmas on the rails: carry food for 6 (no pantry on some runs) and power banks."],
          stay="Train", cost="₹500 food")
    d.day("Day 3 · Sat 26 Dec", "Raxaul → Birgunj", ["Raxaul ~17:00 → rickshaws across the border → <b>Birgunj</b> (Ghantaghar, Gahawa Mai temple). Early night."],
          stay="Birgunj hotel (3 rooms)", cost="₹100 rickshaw + ₹600–900 stay + ₹500 food")
    d.day("Day 4 · Sun 27 Dec", "Birgunj → Kathmandu · Boudhanath + Pashupatinath aarti", [
        "06:30 departure; ~6–8 h through the hills. Check in to the Airbnb near Thamel/Swayambhu.",
        "<b>Boudhanath stupa</b> at golden hour → <b>Pashupatinath evening aarti</b> on the Bagmati ghats (~18:00).",
    ], stay="Airbnb Kathmandu", cost="₹500–1,700 transfer + ₹400 taxis + ₹700 food")
    d.day("Day 5 · Mon 28 Dec", "Swayambhu · Kathmandu, Patan &amp; Bhaktapur Durbar Squares", [
        "Sunrise at <b>Swayambhunath</b> (Monkey Temple) → <b>Kathmandu Durbar Square</b> (Kumari Ghar) → <b>Patan Durbar Square</b> and Patan Museum → "
        "<b>Bhaktapur</b> for sunset, juju dhau (king curd) and Nyatapola temple. Dinner in Thamel.",
        "Show your Indian ID for SAARC-rate tickets (far cheaper than the foreigner rate).",
    ], stay="Airbnb Kathmandu", cost="₹400 taxis + ₹700 entries + ₹800 food")
    d.day("Day 6 · Tue 29 Dec", "Kathmandu → Bandipur (offbeat hill town)", [
        "07:00 tourist bus → Dumre → jeep up to <b>Bandipur</b>: car-free Newari bazaar on a ridge. <b>Tundikhel</b> and <b>Thani Mai</b> viewpoints for "
        "Manaslu and Annapurna at sunset. Optional on the way: Manakamana cable car at Kurintar.",
    ], stay="Bandipur guesthouse / homestay", cost="₹600 transport + ₹700 food")
    d.day("Day 7 · Wed 30 Dec", "Bandipur sunrise → Pokhara · Phewa + Peace Pagoda", [
        "Sunrise at Thani Mai → bus to <b>Pokhara</b> (~2.5 h). <b>Phewa lake</b> boating to Tal Barahi temple → <b>World Peace Pagoda</b> for sunset over the Annapurnas.",
    ], stay="Airbnb Pokhara (Lakeside)", cost="₹250 bus + ₹300 boat + ₹800 food")
    d.day("Day 8 · Thu 31 Dec", "Sarangkot sunrise · caves &amp; falls · NYE street festival", [
        "05:00 taxi to <b>Sarangkot</b> for sunrise on Machhapuchhre/Annapurna. Optional tandem paragliding from Sarangkot (NPR 9,000–12,000).",
        "<b>Davis Falls</b>, <b>Gupteshwor Mahadev cave</b>, International Mountain Museum.",
        "<b>Pokhara Street Festival</b> on Lakeside (usually 28 Dec–1 Jan): food stalls, music, the biggest NYE party in Nepal.",
    ], stay="Airbnb Pokhara", cost="₹300 taxi + ₹1,000 food/NYE")
    d.day("Day 9 · Fri 1 Jan", "Pokhara → Birgunj → Raxaul → Patna", [
        "07:00 day bus to Birgunj (7–9 h) → rickshaw across the border → bus Raxaul → Patna (5–6 h). Long day, so pack snacks and keep phones charged.",
    ], stay="Airbnb / hotel near Patna Jn or Danapur", cost="₹700–1,000 bus + ₹450–600 bus + ₹700–1,000 stay + ₹600 food")
    d.day("Day 10 · Sat 2 Jan", "Patna → train home", ["Optional morning at Gandhi Ghat / Patna Museum. <b>12:15 12792</b> from Danapur."],
          stay="Train", cost="₹600 food")
    d.day("Day 11 · Sun 3 Jan", "Home", ["Secunderabad ~21:30."])

    X.airbnb(d, [
        ["2 (27–28 Dec)", "Kathmandu", "<b>Boutique 3BHK Tibet Designer Apartment</b> (Swayambhu, near Thamel): 5.0★ (~80) · <b>Spacious 3BR near Thamel</b> "
         "4.9★ (30+), 6 guests", "<b>The Magnolia 3BHK</b> (Paknajol) 4.88★ (16) · <b>White House Studio 3BHK</b> (Uttardhoka)", (4000, 6500)],
        ["1 (29 Dec)", "Bandipur", "Not on Airbnb: old Newari guesthouses on the bazaar", "Rooms NPR 2,000–3,500 (₹1,250–2,200) × 3", (3800, 6600)],
        ["2 (30–31 Dec)", "Pokhara (Lakeside)", "<b>Full Lakeview 3BHK Penthouse</b>: 4.91★ (79), 6 guests · <b>Hilltop Villa w/ Private Pool</b> 3BR 4.96★ "
         "(~80), 15 min from Lakeside", "Lakeside rooftop apartment, 1 min to the lake (4.62★, 84; 3rd floor, no lift)", (6000, 10000)],
    ])

    d.h1("Places: main vs offbeat")
    d.table([
        ["Place", "Type", "Why"],
        ["Pashupatinath, Boudhanath, Swayambhunath", "Main (UNESCO)", "Nepal's great temples and stupas"],
        ["Kathmandu, Patan, Bhaktapur Durbar Squares", "Main (UNESCO)", "Newari palaces, woodcarving, juju dhau"],
        ["Bandipur", "Offbeat", "Car-free ridge bazaar, Himalayan sunsets"],
        ["Phewa lake, Peace Pagoda, Sarangkot", "Main", "Annapurna views"],
        ["Davis Falls, Gupteshwor cave", "Main", "Short stops"],
        ["Pokhara Street Festival", "Seasonal", "New Year on Lakeside"],
    ], [0.42, 0.18, 0.4])
    d.h1("Bike / scooty rentals")
    d.table([
        ["Where", "Rates", "Notes"],
        ["Pokhara Lakeside", "Scooty NPR 1,200–1,800/day · 150 cc NPR 1,800–2,500", "Indian DL accepted at most shops; fuel ≈ NPR 175/l. Good for Sarangkot by day"],
        ["Kathmandu (Thamel)", "Scooty NPR 1,200–1,500/day", "Heavy traffic and dust; taxis are easier for 6"],
    ], [0.18, 0.37, 0.45])
    d.h1("What to wear")
    d.p("Kathmandu and Pokhara are 2–20 °C in late December: a fleece + light padded jacket and a cap are enough. Sarangkot at 05:00 and Bandipur "
        "nights are cold (≈ 2–5 °C). No snow gear needed; skip the rentals.")
    d.h1("Budget per person (6 people sharing)")
    d.budget(BUDGET, "Fits ₹25–30k comfortably on SL, and still does in 3A.")
    d.h1("Bookings to do now")
    d.bullets([
        "<b>17005 for 24 Dec today</b> (weekly train). Then 12792 Danapur → Secunderabad for 2 Jan.",
        "Airbnb Pokhara 30–31 Dec (NYE festival demand), then Kathmandu.",
        "Check every adult's passport or voter ID. Photocopies of both, plus 2 photos each.",
    ])
    d.h1("Plan B")
    d.bullets([
        "17005 waitlisted: Hyderabad → Patna/Danapur by 12791 (daily, Secunderabad ~09:25 → Danapur ~18:15 next day) on 24 Dec, then bus Patna → Raxaul.",
        "Fog delays the train into Raxaul: sleep in Birgunj and leave for Kathmandu at dawn as planned.",
        "Want snow-peak views up close: swap Bandipur for Nagarkot (sunrise on the Langtang–Everest range).",
    ])
    X.packing_and_safety(d, ["Use only registered paragliding operators in Pokhara. Avoid night buses on Nepal's mountain highways."])
    d.sources([
        "17005/17006 Hyderabad–Raxaul: ixigo, totaltraininfo, ConfirmTkt, RailMitra, indiantrain (Thu 23:10; Raxaul ~16:50–17:00; 17006 Sun 03:15)",
        "12792/12791 Danapur–Secunderabad: totaltraininfo, ixigo, RailMitra, Trainman (12:15 → 21:30 next day, daily)",
        "Nepal entry documents & Indian currency rules: HappyFares Nepal visa guide 2026, Business Today (Jul 2026), Deccan Chronicle, Niva Bupa",
        "Birgunj–Kathmandu and Kathmandu–Pokhara buses: 12go, Bookaway, The Himalayan Times, bussewa (2026), In Your Pocket; Bandipur via Dumre: hopnepal, kimkim",
        "Pokhara Street Festival dates: The Himalayan Times, Ratopati, Kathmandu Post, Republica",
        "Airbnb listings: airbnb.com Kathmandu/Thamel/Pokhara Lakeside pages via search (Nov 2026)",
        "International comparison: Bhutan SDF (Consulate General of India Phuentsholing, discoverwithdheeraj, maverickbird); HYD–CMB/BKK/KUL fares: "
        "Skyscanner, IndiGo, Air India, AirAsia, Trripah (Nov 2026)",
    ])
    d.build()
    return lo, hi
