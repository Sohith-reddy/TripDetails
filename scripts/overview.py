"""00 Overview: comparison of the 5 plans + all trains/flights + gear + booking strategy."""
from common import PlanDoc
import sections as X
import shared as S


def build(path):
    d = PlanDoc(path,
                "North India Winter Trip: Overview",
                "5 plans compared · Hyderabad ⇄ Delhi trains (early morning + every-halt method) · flights · winter gear buy vs rent · "
                "booking deadlines. Leave 24 Dec 2026, home by 3 Jan 2027 · Budget ₹25–30k per person",
                "#334155", "OVERVIEW · TRAINS · FLIGHTS · GEAR")

    d.h1("The 5 plans side by side")
    d.table([
        ["Plan", "Where", "Snow for these dates", "Offbeat level", "Crowds", "Main transport", "Per person (4 ppl): shoestring / recommended"],
        ["1 · Standard", "Shimla, Kufri, Narkanda–Hatu, Manali, Solang, Atal Tunnel–Sissu, Naggar, Sethan, Kasol", "Good (Solang/Sissu/Hatu)",
         "★★☆☆☆", "High", "Train + HRTC Volvo", "₹24.6k / ₹30.8k"],
        ["2 · Offbeat Himachal", "Mashobra, Shali Tibba, Narkanda, Thanedar, Jalori, Jibhi, Tirthan, Naggar, Sethan", "Good (Hatu/Jalori/Sethan)",
         "★★★★★", "Low", "Train + Volvo + taxis", "₹25.4k / ₹31.2k"],
        ["3 · Kashmir (my pick)", "Srinagar, Gulmarg, Drung, Doodhpathri, Sonamarg, Pahalgam–Aru, Martand", "<b>Best</b> (Chillai Kalan)",
         "★★★☆☆", "Medium", "Train + Vande Bharat to Srinagar", "₹22.7k / ₹30.4k"],
        ["4 · Sikkim", "Gangtok, Tsomgo–Nathula, Silk Route (Zuluk, Nathang), Aritar, Ravangla, Pelling, Rinchenpong, Darjeeling",
         "At passes/lakes only", "★★★★☆", "Low–medium", "Flights to Bagdogra", "₹35.6k / ₹47.3k (lean ≈ ₹31k)"],
        ["5 · Uttarakhand", "Rishikesh, Devprayag, Sari–Deoria Tal, Chopta–Tungnath–Chandrashila, Auli–Gorson, Haridwar", "Good on the trek / Auli",
         "★★★☆☆", "Low–medium", "Train + bus + cab", "₹20.1k / ₹30.3k"],
    ], [0.12, 0.27, 0.13, 0.09, 0.09, 0.13, 0.17])
    d.callout("Recommendation",
              ["<b>Want guaranteed snow on budget → Plan 3 (Kashmir).</b> The new Jammu–Srinagar Vande Bharat makes it a train trip, and Gulmarg/Sonamarg/Aru "
               "are snow-white by late December.",
               "<b>Want quiet villages and no NYE crowd → Plan 2.</b> <b>Want a proper trek → Plan 5</b> (cheapest too). "
               "<b>First trip to the hills, want the classics → Plan 1.</b> "
               "<b>Plan 4 is the most beautiful for mountain views but only fits ₹30k in its lean form</b> because of flights."], "good")
    d.small("Budgets assume 4 travellers sharing rooms (2 per room) and cabs, 3A sleeper for 'recommended', SL + dorms/homestays for 'shoestring'. "
            "Personal shopping and the one-time winter clothing purchase (≈ ₹4–6.5k if you own nothing) are not included.")

    d.h1("Calendar &amp; booking deadlines")
    d.table(S.CALENDAR, [0.14, 0.12, 0.74])
    d.table(S.BOOKING_WINDOW, [0.28, 0.4, 0.32])
    d.callout("Do these 3 things today (4 Nov)",
              ["1. Book the <b>return</b> train (2 Jan): its 60-day window opened yesterday and Telangana Exp / Rajdhani 3A fill within days in the "
               "New Year week.",
               "2. Check the <b>onward</b> train (24 Dec) on all the options below using the every-halt method. If everything is WL beyond ~WL 20 (3A), "
               "book the flight instead today, because flight fares only go up from here.",
               "3. Book NYE-night stays (31 Dec) with free cancellation. They are the first to sell out in every plan."], "warn")

    d.h1("Hyderabad → Delhi trains (all options, early morning first)")
    d.table(S.ONWARD_TRAINS, X.ONWARD_W)
    d.small(S.TELANGANA_HALTS)
    d.space(4)
    d.h2("If Hyderabad stations are full: board further up the line")
    d.table(S.ONWARD_BACKUP, [0.2, 0.25, 0.55])
    d.h2("How to check every halt and actually get a seat")
    d.bullets(S.HALT_METHOD)
    d.callout("Why I can't give you live 'available / WL' numbers here",
              "IRCTC and the seat-availability pages need a login and captcha, and the availability sites were not reachable from this environment. "
              "Everything above (train numbers, days, timings, fares) is researched; the availability check takes 10 minutes with the steps above. "
              "Do it in the ConfirmTkt or ixigo Trains app, which also show WL-confirmation chances and alternate-station suggestions.")

    d.h1("Delhi → Hyderabad (home by 3 Jan)")
    d.table(S.RETURN_TRAINS, X.RETURN_W)

    d.h1("Flights from Hyderabad")
    d.table(S.FLIGHTS, X.FLIGHT_W)
    d.small(S.FLIGHT_NOTE)
    d.space(4)
    d.table([
        ["Mix that saves time", "Extra cost vs all-train", "Days gained in the hills"],
        ["Train out + fly back (Delhi/IXC/SXR/DED → HYD on 2 Jan)", "+₹4–8k", "+1 (Kashmir: +1.5)"],
        ["Fly out + train back", "+₹4–8k", "+1"],
        ["Fly both ways", "+₹10–17k", "+2. Over budget for Plans 1, 2, 3 and 5"],
    ], [0.5, 0.25, 0.25])

    d.h1("Winter gear: full list, buy vs rent")
    d.p(S.GEAR_SUMMARY)
    d.table(S.GEAR_TABLE, [0.2, 0.1, 0.2, 0.3, 0.2])
    d.h2("Where to buy before you leave Hyderabad")
    d.bullets([
        "<b>Decathlon</b> (several stores in Hyderabad, plus online): thermals (Wedze), fleece, Quechua padded jackets, MH100/MH500 shoes, gloves, socks.",
        "Hyderabad's Koti / Begum Bazaar and Sunday markets: cheaper woollens, caps, socks (₹100–300).",
        "Delhi: Sarojini Nagar / Janpath / Monastery Market (Majnu ka Tilla) for cheap jackets if you have a few hours on 25 Dec.",
        "Online rentals that ship to you: Indiahikes rentals (padded jacket rated −10 °C ≈ ₹55–80/day), trek-operator rental shops (₹100/day jackets).",
    ])
    d.h2("Layering for −10 °C (what to wear on a snow day)")
    d.table([
        ["Layer", "What", "Why"],
        ["Base", "Thermal top + bottom (synthetic/merino)", "Keeps sweat off the skin"],
        ["Mid", "Fleece / woollen sweater", "Traps heat"],
        ["Outer", "Padded/down jacket + rented snow suit on snow days", "Wind and wet protection"],
        ["Extremities", "Woollen cap + balaclava, inner + waterproof gloves, 2 pairs of socks, gumboots/trek shoes, UV sunglasses", "Hands, feet, ears and eyes go first"],
    ], [0.15, 0.55, 0.3])

    d.h1("Carry list &amp; safety")
    X.packing_and_safety(d)

    d.h1("What's in each PDF")
    d.bullets([
        "Overview (this file): comparison, all trains and flights, every-halt method, gear.",
        "Each plan PDF: how to get there and back for that plan, local transport with prices, a day-by-day itinerary with stay and spend per day, "
        "main vs offbeat places, bike/scooty rentals with rates and rules, gear rental points on that route, an itemised budget, "
        "what to book now, a Plan B for snow and traffic, and sources.",
    ])
    d.sources([
        "IRCTC 60-day ARP (from 1 Nov 2024) & 2026 Aadhaar-verified booking updates: Business Today, India TV, Upstox, Trainman blog, india.com, Patrika, DeshGujarat",
        "Hyderabad–Delhi train data: Wikipedia (Telangana Exp, Secunderabad Rajdhani, Duronto, Dakshin Exp), ConfirmTkt, totaltraininfo, ixigo, Trainman, RailMitra, gettraininfo, travelkhana, etrain.info, indiantrain.in",
        "22691/22692 Bengaluru Rajdhani at Secunderabad: ConfirmTkt, RailMitra, travelkhana",
        "22705/22706 Humsafar: ixigo, RailMitra, NativePlanet, Goibibo, Adani One (running days conflict; verify)",
        "Vande Bharat Sleeper Delhi–Secunderabad: not launched as of Hyderabad Mail (2 Nov 2026); Charlapalli–Nizamuddin specials 07023/07021: indiarailinfo, Curly Tales",
        "Flights: MakeMyTrip, Goibibo, ixigo, Skyscanner, HappyFares, Air India / Air India Express route pages, IndiGo route pages, flightconnections (Nov 2026)",
        "Gear rental rates: Indiahikes rentals, Himalayan Hikers, Himalayan Dream Treks, SharePal, travelcoffee.in, cliffhangersindia, Tripoto",
    ])
    d.build()
