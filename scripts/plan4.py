"""Plan 4: Sikkim (Gangtok, Tsomgo, Silk Route: Zuluk, Nathang, Aritar; Ravangla, Pelling, Rinchenpong) + Darjeeling."""
from common import PlanDoc
import sections as X


def build(path):
    d = PlanDoc(path,
                "Plan 4 · Sikkim: Gangtok, Silk Route &amp; West Sikkim",
                "Gangtok, Tsomgo Lake &amp; Nathula, the Old Silk Route (Zuluk, Thambi, Nathang, Kupup), Aritar, Ravangla, Pelling, "
                "Rinchenpong, Darjeeling. 24 Dec 2026 – 3 Jan 2027 · Fly Hyderabad ↔ Bagdogra",
                "#b45309", "PLAN 4 · SIKKIM & DARJEELING")

    d.h1("At a glance")
    d.table([
        ["Route", "HYD ✈ Bagdogra → Gangtok 3N → Zuluk 1N (Silk Route) → Aritar 1N → Ravangla 1N → Pelling 1N → Rinchenpong 1N (NYE) → "
                  "Darjeeling 2N → Bagdogra ✈ HYD"],
        ["Snow chances", "High: Tsomgo, Nathula, Nathang, Kupup (often frozen lakes). Low–medium: Zuluk. None in Gangtok, Pelling, Darjeeling "
                         "(but clear Kanchenjunga views are best in Dec–Jan)"],
        ["Crowd level", "Medium in Gangtok and Darjeeling (Christmas/NYE). Low on the Silk Route, Aritar, Ravangla, Rinchenpong"],
        ["Difficulty", "Easy, but high altitude: Nathula 4,310 m, Nathang ~4,100 m. Slow down and stay hydrated"],
        ["Temperatures", "Gangtok 4–13 °C · Pelling/Darjeeling 2–11 °C · Zuluk/Nathang −12 to 0 °C"],
        ["Budget (per person, 4 people)", "≈ ₹35.6k shoestring · ≈ ₹47k comfortable · ≈ ₹31k 'lean version' (see box). "
                                          "<b>Flights make this the costliest plan.</b>"],
    ], [0.22, 0.78], header=False, bold_first_col=True)

    d.callout("Honest budget note",
              ["Trains from Hyderabad to New Jalpaiguri take 35–42 h and their weekly days don't line up with 24 Dec (e.g. 15645 Charlapalli–Silchar "
               "via NJP runs Wed/Sat; 07572 special runs Fri). With only 10 days, <b>flying both ways is the practical choice</b>, and that alone "
               "is ₹13–17k.",
               "<b>Lean version to get close to ₹30k:</b> book flights now (aim ≤ ₹6,500 each way), travel as 6 in one Bolero/Sumo, use hostel dorms "
               "in Gangtok, take a shared seat to Tsomgo (skip Nathula), and do Gangtok 3N → Silk Route 2N → Pelling 3N → Siliguri, dropping "
               "Ravangla, Rinchenpong and Darjeeling (≈ ₹31k)."], "warn")

    d.h1("Getting there and back")
    X.flights(d, (4,), "Flights Hyderabad ⇄ Bagdogra (main way in and out)")
    d.table([
        ["Leg", "Option", "Time", "Approx cost"],
        ["Bagdogra (IXB) → Gangtok", "Reserved cab (small ₹3,000–3,500; SUV ₹3,500–4,500) or auto to Siliguri SNT / Panitanki "
         "then shared Sumo (₹400–550 per seat). Shared cabs don't wait at the airport", "4–5 h (125 km)", "₹600–1,125 pp"],
        ["Bagdogra luxury shared seat", "Wizzride-type shared SUV seat from IXB/NJP", "4–5 h", "₹900–1,200 per seat"],
        ["Darjeeling → Bagdogra", "Reserved cab or shared jeep to Siliguri (₹250–350) + auto/taxi to IXB", "3–3.5 h", "₹450–875 pp"],
    ], [0.22, 0.48, 0.13, 0.17])
    d.h2("Trains via New Jalpaiguri (only if you can leave or return on matching days)")
    d.table([
        ["Train", "From Hyderabad", "Runs", "Duration", "Notes"],
        ["15645 Charlapalli–Silchar Exp (via NJP)", "Charlapalli 16:25", "Wed / Sat (sources differ)", "~35.5 h to NJP", "23 Dec Wed would be a day early"],
        ["15673 Kacheguda–NJP Amrit Bharat", "Kacheguda 19:40", "Weekly (verify)", "~41 h", "Non-AC, cheapest (SL-type)"],
        ["07572 Secunderabad–NJP special", "Secunderabad 06:50", "Fri (seasonal)", "~38 h", "Special train; may not run in Dec"],
        ["12513/12514 Secunderabad ⇄ Guwahati/Silchar SF", "Secunderabad", "Weekly", "~35 h to NJP", "Return 12514 from Guwahati Thu, so NJP Thu → SC Sat 04:00"],
    ], [0.27, 0.17, 0.17, 0.14, 0.25])
    d.small("Alternative: fly Hyderabad → Kolkata (often ₹4–5.5k) + Vande Bharat Howrah → NJP (05:55 → 13:25, CC ≈ ₹1,500). Same cost as a "
            "direct Bagdogra flight but loses half a day. Only worth it if Bagdogra fares jump above ₹10k.")

    d.h1("Permits (Indian citizens)")
    d.table([
        ["Where", "Permit", "How", "Cost"],
        ["Gangtok, Ravangla, Pelling, Rinchenpong", "None", "—", "—"],
        ["Tsomgo Lake + Baba Mandir", "Protected Area Permit", "Registered agent / your hotel applies a day before (submit ID + photos by ~13:00 at "
         "MG Marg Tourist Info Centre). No solo permits; groups only", "Included in the cab fare"],
        ["Nathula Pass", "Separate Nathula endorsement", "Via registered agent, 1-day validity. Indians only. Usually closed Mon/Tue; snow can shut it", "Govt fixed cab fare ₹6,500 (normal) / ₹7,000 (luxury) incl. permits"],
        ["Silk Route: Zuluk, Nathang, Kupup", "Restricted Area Permit", "Through your Zuluk homestay/driver; issued at Rongli police station on the way", "≈ ₹200–300 pp + vehicle pass"],
        ["Lachung / Yumthang / Zero Point (optional swap)", "PAP", "Package from Gangtok. Reopening dates vary by report and heavy snow often closes it", "₹4,000–6,000 pp 2D/1N package"],
    ], [0.24, 0.16, 0.42, 0.18])
    d.small("Carry 4 passport photos and 2 Aadhaar copies per person. Permit counters close early, so give documents to the agent on arrival day.")

    d.h1("Day-by-day itinerary")
    d.day("Day 1 · Thu 24 Dec", "Hyderabad ✈ Bagdogra → Gangtok", [
        "Morning IndiGo flight (~2 h 20 m). Taxi/shared cab to Gangtok (4–5 h along the Teesta, Rangpo checkpost, no permit for Gangtok).",
        "Hand over ID + photos to your hotel/agent tonight for the Tsomgo/Nathula permit on Day 3.",
        "Christmas Eve on <b>MG Marg</b> (lit up, no vehicles).",
    ], stay="Gangtok budget hotel / hostel (₹1,500–2,800 per room; dorm ₹500–700)", cost="₹875 cab share + ₹600 food")
    d.day("Day 2 · Fri 25 Dec", "Gangtok sightseeing (full-day cab ₹3,000–3,500)", [
        "<b>Rumtek monastery</b> (Dharma Chakra Centre) → <b>Lingdum (Ranka) monastery</b> (offbeat, quiet) → Banjhakri falls → "
        "Namgyal Institute of Tibetology → Do Drul Chorten → Enchey monastery.",
        "<b>Tashi viewpoint</b> / <b>Ganesh Tok</b> / <b>Hanuman Tok</b> for Kanchenjunga at sunset. Gangtok ropeway (short ride).",
        "Evening: MG Marg Christmas, momos and thukpa at Lal Market side.",
    ], stay="Gangtok", cost="₹800 cab share + ₹300 entries + ₹700 food")
    d.day("Day 3 · Sat 26 Dec", "Tsomgo Lake · Baba Mandir · Nathula (snow day)", [
        "Leave 07:00 (permit vehicle). <b>Tsomgo (Changu) Lake</b>, 3,753 m, often frozen in December. Rent boots/coats at the lake stalls (₹100–200). Yak ride optional.",
        "<b>Baba Harbhajan Singh Mandir</b>, and <b>Nathula</b> (4,310 m; Indo-China border, Indians only) if permitted. Govt fixed cab fare ₹6,500–7,000 incl. permits. "
        "Tsomgo-only trips ≈ ₹4,500–5,500 per car or ₹1,000–1,500 per shared seat.",
        "Back by 15:00. Rest; altitude headaches are common.",
    ], stay="Gangtok", cost="₹1,700 cab share + ₹200 rent + ₹700 food")
    d.day("Day 4 · Sun 27 Dec", "Gangtok → Rongli (permit) → Zuluk · Old Silk Route", [
        "Reserved vehicle for 2 days (≈ ₹10,000–14,000 incl. permits; your Zuluk homestay can arrange). Gangtok → Rongli (permit) → Lingtam → "
        "Padamchen → <b>Zuluk (2,850 m)</b>, about 4 h.",
        "Afternoon: <b>Lungthung</b> and the view over the 32 hairpin bends of the Zuluk road.",
    ], stay="Zuluk homestay with all meals (₹1,000–1,500 pp)", cost="₹1,750 vehicle share + permit")
    d.day("Day 5 · Mon 28 Dec", "Thambi sunrise · Nathang valley · Kupup → Aritar", [
        "04:45 drive to <b>Thambi viewpoint</b> for Kanchenjunga sunrise over the zig-zag road.",
        "<b>Nathang valley</b> (~4,100 m, often snowy, −10 °C), <b>Kupup / Elephant lake</b> (frozen), <b>Old Baba Mandir</b>, Tukla valley memorial.",
        "Descend to <b>Aritar</b>: <b>Lampokhari lake</b> (boot-shaped lake, boating), <b>Mankhim</b> viewpoint, Aritar gumpa.",
    ], stay="Aritar homestay / lake-side lodge (₹1,500–2,500 per room)", cost="₹1,750 vehicle share + ₹700 food")
    d.day("Day 6 · Tue 29 Dec", "Aritar → Temi → Ravangla", [
        "Drive via Rorathang–Singtam (≈ ₹3,500 per car, or shared jeeps with 1–2 changes).",
        "<b>Temi Tea Garden</b> (Sikkim's only tea estate), <b>Buddha Park (Tathagata Tsal)</b> with its 130 ft Buddha, <b>Ralang monastery</b> (offbeat).",
    ], stay="Ravangla homestay (₹1,200–2,000 per room)", cost="₹875 cab share + ₹100 entry + ₹700 food")
    d.day("Day 7 · Wed 30 Dec", "Ravangla → Pelling (West Sikkim)", [
        "Shared jeep via Legship (₹200–300) or cab (₹2,800–3,500).",
        "<b>Pelling Skywalk &amp; Chenrezig statue</b>, <b>Pemayangtse monastery</b>, <b>Rabdentse ruins</b> (17th-c. capital), sunset over Kanchenjunga.",
    ], stay="Pelling budget hotel (₹1,500–2,500 per room)", cost="₹700 transfer share + ₹200 entries + ₹700 food")
    d.day("Day 8 · Thu 31 Dec", "Khecheopalri lake · Kanchenjunga falls → Rinchenpong (quiet NYE)", [
        "Half-day cab: <b>Khecheopalri (wishing) lake</b>, <b>Kanchenjunga falls</b>, Rimbi falls.",
        "Short drive to <b>Rinchenpong</b> (offbeat): <b>Resum monastery</b> walk, Poison Lake, Kaluk. Kanchenjunga sunset across the valley. "
        "NYE bonfire at a homestay.",
    ], stay="Rinchenpong homestay (₹1,200–2,000 per room)", cost="₹1,125 cab share + ₹800 food/NYE")
    d.day("Day 9 · Fri 1 Jan", "Rinchenpong → Jorethang → Darjeeling", [
        "≈ 4 h via Jorethang (shared jeeps via Jorethang ₹400–500 total, or cab ₹4,000–5,000).",
        "Evening: Chowrasta, Mall Road, Glenary's / Keventer's, Darjeeling tea shops.",
    ], stay="Darjeeling (₹1,500–2,500 per room; NYE-week rates)", cost="₹500–1,125 transfer + ₹700 food")
    d.day("Day 10 · Sat 2 Jan", "Tiger Hill sunrise · Toy train · Darjeeling", [
        "04:00 <b>Tiger Hill</b> sunrise over Kanchenjunga (shared jeep or cab ₹1,500–2,000) → <b>Ghoom monastery</b> → <b>Batasia Loop</b>.",
        "<b>DHR toy train joyride</b> Darjeeling–Ghum (UNESCO; ₹800–1,500, book on IRCTC; festive specials run till 3 Jan 2027).",
        "Japanese Peace Pagoda, Happy Valley tea estate, HMI + Padmaja Naidu zoo (closed Thursdays).",
    ], stay="Darjeeling", cost="₹500 cab share + ₹1,000 toy train + ₹700 food")
    d.day("Day 11 · Sun 3 Jan", "Darjeeling → Bagdogra ✈ Hyderabad", [
        "Leave by 07:00 (3–3.5 h; fog in the plains can slow you down). Take a midday/afternoon flight, not an early-morning one.",
    ], cost="₹450–875 transfer")

    d.h1("Offbeat vs main in this plan")
    d.table([
        ["Place", "Type", "Why"],
        ["Gangtok MG Marg, Rumtek, Tashi viewpoint", "Main", "Capital, monasteries, Kanchenjunga views"],
        ["Lingdum monastery", "Offbeat", "Large, quiet monastery 20 km from Gangtok"],
        ["Tsomgo Lake, Baba Mandir, Nathula", "Main", "Frozen lake, border pass, snow"],
        ["Zuluk, Thambi, Nathang, Kupup", "Offbeat", "Old Silk Route: zig-zag road, high snow valley, frozen lakes"],
        ["Aritar (Lampokhari, Mankhim)", "Offbeat", "Lake village in East Sikkim"],
        ["Temi tea garden, Ravangla Buddha Park, Ralang", "Semi-offbeat", "Tea slopes and monasteries"],
        ["Pelling (Skywalk, Pemayangtse, Rabdentse)", "Main", "West Sikkim's Kanchenjunga balcony"],
        ["Khecheopalri, Kanchenjunga falls", "Main", "Sacred lake, waterfalls"],
        ["Rinchenpong, Resum, Kaluk", "Offbeat", "Quiet ridge villages with big mountain views"],
        ["Darjeeling: Tiger Hill, toy train, Batasia", "Main", "Classic hill station"],
    ], [0.4, 0.15, 0.45])

    d.h1("Bike / scooty rentals")
    d.table([
        ["Where", "Rates", "Rules / advice"],
        ["Siliguri (most choice)", "Scooty ₹500–800 · 150–350 cc ₹900–1,800", "WB-registered rentals can ride to Gangtok. For Tsomgo/Nathula/Silk Route, "
         "permits are needed and outside-state vehicles may be refused (Sikkim is also considering limits on two-wheelers in permit areas). "
         "Get written confirmation from the rental shop"],
        ["Gangtok", "Scooty ≈ ₹699 per 24 h · bikes ₹1,200–2,000", "Fuel/tolls/parking extra. Fine for Gangtok–Rumtek–Ranka on dry days"],
        ["Pelling / Darjeeling", "Limited; ₹700–1,500", "Steep roads and early dark (17:00). Taxis are simpler"],
    ], [0.2, 0.3, 0.5])
    d.p("<b>Advice:</b> don't ride to Tsomgo, Nathula or Zuluk in December. Frozen roads above 3,000 m and permit rules make reserved local vehicles "
        "with experienced drivers the right call.")

    X.gear(d, [
        ["Point", "What you can rent", "Rate"],
        ["Tsomgo Lake stalls (on the way)", "Long coats, gumboots, gloves", "₹100–200 per item"],
        ["Zuluk / Nathang", "Few rentals; homestays may lend gumboots", "Carry your own warm layers"],
        ["Lachung (if you swap in North Sikkim)", "Snow boots", "≈ ₹100 per pair"],
        ["Gangtok Lal Market / Darjeeling Mall (buy)", "Cheap jackets, gloves, caps", "₹300–1,500"],
    ])

    d.h1("Budget (per person, 4 people)")
    d.budget([
        ("Flight Hyderabad → Bagdogra", 6500, 8500, "Book now; 24 Dec fares climb"),
        ("Flight Bagdogra → Hyderabad", 6500, 8500, ""),
        ("Bagdogra → Gangtok", 600, 875, "Shared vs reserved"),
        ("Gangtok sightseeing cab", 800, 800, ""),
        ("Tsomgo (+ Nathula)", 1200, 1700, "Shared seat Tsomgo only vs govt-fixed Nathula cab"),
        ("Silk Route vehicle 2 days incl. permits", 3000, 3500, ""),
        ("Aritar → Ravangla → Pelling (+ Pelling local)", 1600, 2250, "Shared jeeps vs cabs"),
        ("Pelling → Rinchenpong → Darjeeling", 800, 1575, ""),
        ("Darjeeling local + transfer to Bagdogra", 850, 1375, ""),
        ("Stays, 10 nights", 7500, 10000, "Dorms/homestays vs rooms (2 per room)"),
        ("Food", 4500, 5000, "Zuluk homestay includes meals"),
        ("Toy train joyride", 0, 1000, "Optional"),
        ("Entries, permits, misc", 500, 700, ""),
        ("Gear rentals", 400, 500, ""),
        ("Buffer", 800, 1000, ""),
    ], "Over the ₹25–30k limit because of flights. A group of 6 saves ≈ ₹4k pp. The lean version (box above) comes to ≈ ₹31k.")

    d.h1("Bookings to do now")
    d.bullets([
        "Flights HYD⇄IXB (24 Dec out, 3 Jan midday back). Check IndiGo directly; fares rise every week from here.",
        "Gangtok hotel for 24–27 Dec through someone who can also arrange the Tsomgo/Nathula permit vehicle.",
        "Zuluk homestay (they arrange the Silk Route vehicle + Rongli permit), Darjeeling for 1–2 Jan (NYE-week demand).",
        "DHR joyride on IRCTC ~2–3 weeks ahead.",
    ])
    d.h1("Plan B")
    d.bullets([
        "Nathula closed (snow/days): Tsomgo + Baba Mandir only (cheaper), or Hanuman Tok + Ganesh Tok half-day.",
        "Silk Route snowed in above Zuluk: stay low (Aritar + Rolep/Reshi), or swap to <b>Okhrey / Hee-Bermiok</b> in West Sikkim, or Lachung if it's open.",
        "Want North Sikkim (Lachung–Yumthang–Zero Point)? Swap Days 4–5 for a 2D/1N Gangtok package. Status changed several times in 2025–26 "
        "and Zero Point is often closed by snow, so confirm the week before.",
    ])
    X.packing_and_safety(d, [
        "High altitude (Nathula, Nathang): no alcohol the night before, climb slowly, carry dry fruits and water; turn back if headache + nausea worsen.",
        "Sikkim bans plastic bottles at many tourist spots. Carry a refillable bottle.",
    ])
    d.sources([
        "Nathula/Tsomgo fixed taxi fares (₹6,500/₹7,000 incl. permits): India Today NE, Outlook Traveller, Club Mahindra (2024 order)",
        "Permit process and Silk Route permit at Rongli: muddietrails Sikkim permits, trekkingsikkim, darjeeling-tourism.com",
        "North Sikkim reopening reports (conflicting 2025–26 dates): WanderOn, UNI India, sikkimdarjeelingtourism, muddietrails",
        "Bagdogra/NJP → Gangtok shared & reserved rates: darjeeling-tourism.com, banbanjara, darjeelingtravels.in (2026)",
        "Bike rules: bikewalebhaiya.com Sikkim guides, ridesiliguri, newkerala (Sikkim mulls two-wheeler limits, Aug 2026)",
        "Trains to NJP (15645, 15673, 07572, 12513): erail/gettraininfo/ixigo/railyatri listings via search (running days conflict)",
        "DHR toy train joyride fares & festive specials till 3 Jan 2027: Outlook Traveller, Curly Tales, ETV Bharat, RailMitra",
        "HYD–IXB flights: IndiGo route page, HappyFares, Skyscanner, Kayak (Nov 2026)",
        "Winter offbeat ideas (Zuluk, Kecheopalri, Lachung boots): TravelTriangle, Thrillophilia, Tripoto traveller notes",
    ])
    d.build()
