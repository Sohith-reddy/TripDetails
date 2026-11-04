"""00 Overview: all plans compared + trains (incl. Kazipet/Warangal/Vijayawada), toy train, flights, vehicles for 6, Airbnb, gear."""
from common import PlanDoc, k
import sections as X
import shared as S

PLANS = [
    ("1 · Standard Shimla–Manali", "Toy train to Shimla, Kufri, Narkanda–Hatu, Manali, Solang, Atal Tunnel–Sissu, Naggar, Sethan, Kasol",
     "Good", "★★☆☆☆", "High", "Train + toy train + HRTC"),
    ("2 · Offbeat Shimla–Manali", "Toy train, Mashobra, Shali Tibba, Narkanda, Thanedar, Jalori, Jibhi, Tirthan, Sethan NYE",
     "Good", "★★★★★", "Low", "Train + toy train + 1 Innova"),
    ("3 · Kashmir", "Vande Bharat to Srinagar, Gulmarg, Drung, Doodhpathri, Sonamarg, Pahalgam–Aru, Martand", "<b>Best</b>", "★★★☆☆", "Medium",
     "Train all the way"),
    ("4 · Sikkim + Darjeeling", "Gangtok, Tsomgo–Nathula, Silk Route (Zuluk, Nathang), Aritar, Ravangla, Pelling, Rinchenpong, Darjeeling",
     "At passes only", "★★★★☆", "Low–medium", "Flights to Bagdogra"),
    ("5 · Uttarakhand", "Rishikesh, Devprayag, Deoria Tal, Chopta–Tungnath–Chandrashila, Auli–Gorson, Haridwar", "Good (trek/Auli)", "★★★☆☆",
     "Low–medium", "Train + bus + 1 Innova"),
    ("6 · Amritsar + Kangra (new)", "Golden Temple, Wagah, Dalhousie–Khajjiar–Dainkund, McLeodganj–Triund, Palampur, Bir, Kangra toy train",
     "Medium", "★★★☆☆", "Medium", "Train + Innova legs"),
    ("7 · Kinnaur winter (new)", "Toy train both ways, Narkanda, Sarahan, Sangla, Kalpa, Nako, Shimla NYE", "Very good", "★★★★★", "Very low",
     "Train + toy train + 1 Innova"),
    ("8 · Nepal overland (international)", "Kathmandu (3 Durbar Squares, Pashupati, Boudha), Bandipur, Pokhara street festival",
     "No snow (peak views)", "★★★☆☆", "Medium", "Weekly Raxaul train + buses"),
]


def build(path, plan_totals):
    d = PlanDoc(path,
                "North India Winter Trip: Overview (6 people)",
                "8 plans compared (7 North India + Nepal) · trains from Hyderabad, Kazipet, Warangal and Vijayawada · Delhi → Kalka → toy train "
                "connections · Airbnb approach · vehicles for 6 · international options checked · winter gear. 24 Dec 2026 – 3 Jan 2027",
                "#334155", "OVERVIEW · 6 PEOPLE")

    d.h1("All plans side by side (per person, 6 sharing)")
    rows = [["Plan", "Where", "Snow", "Offbeat", "Crowds", "Transport", "Shoestring / recommended"]]
    for i, (name, where, snow, off, crowd, mode) in enumerate(PLANS, start=1):
        lo, hi = plan_totals[i]
        rows.append([f"<b>{name}</b>", where, snow, off, crowd, mode, f"<b>{k(lo)}</b> / {k(hi)}"])
    d.table(rows, [0.14, 0.28, 0.1, 0.1, 0.1, 0.13, 0.15])
    d.callout("Recommendation",
              ["<b>Guaranteed snow → Plan 3 (Kashmir).</b> <b>Offbeat + toy train → Plan 2</b> or <b>Plan 7 (Kinnaur)</b>. <b>Cheapest → Plan 5.</b> "
               "<b>Classic first trip → Plan 1.</b> <b>Something different → Plan 6</b> (Golden Temple + Himachal). <b>Abroad → Plan 8 (Nepal)</b>, the "
               "only international trip that fits the budget.",
               "Plan 4 (Sikkim) is beautiful but needs flights, so it goes over ₹30k unless you take the lean version."], "good")
    d.small("Budgets: 6 travellers, 3-bedroom Airbnbs (or 3 homestay rooms), one Innova or taxi-union SUV per circuit. 'Shoestring' = SL trains, ordinary "
            "buses, cheaper Airbnbs. 'Recommended' = 3A, Volvo, better-rated stays. The one-time winter clothing purchase (≈ ₹4–6.5k if you own "
            "nothing) is not included.")

    d.h1("What changed in this version")
    d.bullets([
        "<b>Group of 6:</b> every cab, Airbnb and Innova cost is split 6 ways. Tatkal tickets need 2 PNRs (max 4 per Tatkal PNR).",
        "<b>Airbnb instead of hotels:</b> each plan lists a best-rated and a budget Airbnb for every stop, with rating, reviews, capacity and an "
        "estimated December price for 6. Where Airbnb has nothing (Zuluk, Sari, Sangla, Bandipur…), homestays are named instead.",
        "<b>Shimla by toy train from Kalka</b> (Plans 1, 2, 7). Default: Telangana Exp → Delhi sightseeing day → 21:10 Kalka Mail → 05:20–06:20 toy train "
        "(≈ ₹265 pp in trains). Fast option: Tamil Nadu Exp from Kazipet → 07:40 Kalka Shatabdi → 12:10 Himalayan Queen (Shimla 25 Dec evening).",
        "<b>Boarding at Kazipet, Warangal and Vijayawada</b> is now in the train tables with times, plus how to get there with 6 people.",
        "<b>Cheapest intermediate trains:</b> SL on overnight Delhi → Kalka / Jammu / Amritsar / Haridwar runs, 2S on the toy train.",
        "<b>New plans:</b> 6 (Amritsar + Kangra valley), 7 (Kinnaur by toy train), 8 (Nepal overland). International and other options that "
        "don't fit are explained at the end.",
    ])

    d.h1("Calendar &amp; booking deadlines")
    d.table(S.CALENDAR, [0.14, 0.12, 0.74])
    d.table(S.BOOKING_WINDOW, [0.32, 0.38, 0.3])
    d.small(S.PNR_NOTE)
    d.space(3)
    d.callout("Do these today (4 Nov)",
              ["1. <b>Return train for 2 Jan</b> (window opened 3 Nov). For Nepal: <b>17005 for 24 Dec</b> (weekly) + 12792 for 2 Jan.",
               "2. <b>Onward train for 24 Dec</b> using the station-by-station check below, then the 25 Dec connection (Kalka Mail / Jammu Mail / "
               "Amritsar train) and the toy train for 26 Dec.",
               "3. <b>NYE-night Airbnbs (30 Dec–1 Jan)</b> with flexible cancellation. Hosts set minimum stays and these sell out first."], "warn")

    d.h1("Hyderabad → Delhi on 24 Dec: every boarding option")
    d.table(S.ONWARD_TRAINS, X.ONWARD_W)
    d.small(S.TO_KAZIPET)
    d.space(2)
    d.small(S.TELANGANA_HALTS)
    d.space(3)
    d.h2("How to check every station and halt and actually get 6 seats")
    d.bullets(S.HALT_METHOD + [S.PNR_NOTE])
    d.callout("Why there are no live 'available / WL' numbers here",
              "IRCTC, ConfirmTkt, erail and Airbnb pages can't be opened from this environment (blocked), so train numbers, days, times and fares come "
              "from search results across several timetable sites. The availability check takes ~10 minutes in the ConfirmTkt or ixigo app, which "
              "also shows confirmation chances and alternate stations.", "info")

    d.h1("Delhi → Kalka → Shimla toy train")
    d.table(S.DELHI_KALKA, X.DK_W)
    d.small(S.DELHI_KALKA_NOTE)
    d.space(3)
    d.table(S.TOY_TRAIN, [0.11, 0.19, 0.13, 0.13, 0.2, 0.24])
    d.small(S.TOY_NOTE)
    d.space(3)
    d.callout("The Delhi gap on 25 Dec", S.HELPFUL_DELHI_DAY, "info")

    d.h1("Back to Hyderabad by 3 Jan")
    d.table(S.RETURN_TRAINS, X.RETURN_W)

    d.h1("Flights (only where they help)")
    d.table(S.FLIGHTS, X.FLIGHT_W)
    d.small(S.FLIGHT_NOTE)

    d.h1("Getting around as 6")
    d.table(S.VEHICLES, [0.2, 0.14, 0.3, 0.14, 0.22])

    d.h1("Airbnb: how to get best-rated and cheapest for 6")
    d.bullets(S.AIRBNB_HOWTO)
    d.small(S.AIRBNB_NOTE)

    d.h1("International trips checked")
    d.table(S.INTERNATIONAL, [0.15, 0.25, 0.25, 0.17, 0.18])
    d.small("Visa notes (Nov 2026 reports): Nepal and Bhutan need no visa for Indians (passport or voter ID). Sri Lanka has a free ETA for Indians. "
            "Malaysia is visa-free till 31 Dec 2026, so travel after that needs checking. Thailand's visa-free stay for Indians is being cut to 30 days. "
            "Vietnam needs an e-visa.")
    d.h2("Other North India options considered")
    d.table(S.OTHER_NORTH, [0.3, 0.7])

    d.h1("Winter gear: buy vs rent")
    d.p(S.GEAR_SUMMARY)
    d.table(S.GEAR_TABLE, [0.2, 0.1, 0.2, 0.3, 0.2])
    d.h2("Where to buy before you leave Hyderabad")
    d.bullets([
        "<b>Decathlon</b> (several Hyderabad stores, plus online): thermals, fleece, padded jackets, MH100/MH500 shoes, gloves, socks.",
        "Koti / Begum Bazaar / Sunday markets: cheaper woollens, caps, socks (₹100–300).",
        "Delhi on 25 Dec: Monastery Market (Majnu ka Tilla), Janpath and Sarojini Nagar for cheap jackets.",
    ])
    X.packing_and_safety(d)
    d.sources([
        "IRCTC 60-day ARP & 2026 Aadhaar-verified booking: Business Today, India TV, Upstox, Trainman blog, india.com, Patrika",
        "Kazipet/Warangal/Vijayawada timings (12621, 12625, 12615, 12721, 22691): ConfirmTkt, ixigo, Goibibo, Paytm, MakeMyTrip, indiarailinfo, RailMitra",
        "Kalka Mail / Kalka Shatabdi / toy train: Cleartrip, RailMitra, indiantrain, totaltraininfo, ixigo, Bajaj Finserv, travelcoffee 2026, Shimla Tourism, exploreindia",
        "17005/17006 & 12791/12792: ixigo, totaltraininfo, ConfirmTkt, RailMitra, Trainman; Jammu Mail 14033: ConfirmTkt, indiantrain",
        "Vande Bharat Jammu–Srinagar: Kashmir Life, NewsX, Inshorts (2026); Kangra toy train restoration: Outlook Traveller, Curly Tales (June 2026)",
        "Vehicle rates: Rajputana Cabs, Triveni Cabs (2026); Airbnb listings via airbnb.com/.co.in search results (Nov 2026)",
        "International: Consulate General of India Phuentsholing (Bhutan SDF), HappyFares/Business Today (Nepal), Skyscanner/IndiGo/AirAsia/Trripah fares, "
        "Esquire India, Skyscanner cheapest-countries guide",
        "Spiti winter: discoverwithdheeraj, treksandtrails, Spiti Holiday Adventure; Kinnaur winter: vargiskhan, travelcoffee",
    ])
    d.build()
