# North India Winter Trip: 24 Dec 2026 – 3 Jan 2027

Leaving Hyderabad 24 Dec (morning is fine), back home by 3 Jan. Budget is ₹25–30k per person.

## The PDFs (in `PDFs/`)

| File | What's inside | Per person (4 travellers): shoestring / recommended |
|---|---|---|
| `00_Overview_Trains_Flights_Gear_Budget.pdf` | Comparison of all 5 plans, every Hyderabad ⇄ Delhi train option (early morning first), how to check availability at every halt, return trains, flights, full winter-gear buy/rent list, booking deadlines | n/a |
| `01_Plan1_Standard_Shimla_Manali.pdf` | Standard plan: Shimla, Kufri, Narkanda–Hatu, Manali, Solang, Atal Tunnel–Sissu, Naggar, Jana, Sethan, Kasol–Manikaran | ₹24.6k / ₹30.8k |
| `02_Plan2_Offbeat_Shimla_Manali_Jibhi_Tirthan.pdf` | Offbeat Shimla–Manali: Mashobra, Shali Tibba, Narkanda, Thanedar, Jalori/Serolsar, Jibhi, Tirthan, Sethan NYE | ₹25.4k / ₹31.2k |
| `03_Plan3_Kashmir_Winter_Gulmarg_Sonamarg_Pahalgam.pdf` | My pick for "North": Kashmir by train (new Jammu–Srinagar Vande Bharat), Gulmarg, Drung, Doodhpathri, Sonamarg, Pahalgam–Aru, Martand | ₹22.7k / ₹30.4k |
| `04_Plan4_Sikkim_Gangtok_SilkRoute_Pelling_Darjeeling.pdf` | Sikkim: Gangtok, Tsomgo–Nathula, Silk Route (Zuluk, Nathang), Aritar, Ravangla, Pelling, Rinchenpong, Darjeeling | ₹35.6k / ₹47.3k (lean version ≈ ₹31k) |
| `05_Plan5_Uttarakhand_Rishikesh_Chopta_Tungnath_Auli.pdf` | Uttarakhand: Rishikesh, Devprayag, Deoria Tal, Chopta–Tungnath–Chandrashila snow trek, Auli–Gorson, Haridwar (+ Kedarkantha / Kumaon variants) | ₹20.1k / ₹30.3k |

Each plan PDF has: how to get there and back, local transport with prices, a day-by-day itinerary (stay + spend per day), main vs offbeat places,
bike/scooty rental rates and rules, winter-gear rental points on that route, an itemised budget, what to book now, a Plan B, and sources.

## Book first (as of 4 Nov 2026)

1. **Return train for 2 Jan.** Booking opened 3 Nov (60-day rule). Options: 12724 Telangana Exp (New Delhi 16:00 → Hyderabad ~17:10 next day) or 22692 Rajdhani.
2. **Onward train for 24 Dec** (Thursday): 12723 Telangana Exp 06:00 from Hyderabad Deccan, 22691 Rajdhani 07:10 from Secunderabad,
   or 12285 Duronto 12:50 from Secunderabad (Sun/Thu). If they show a waitlist, follow the halt-by-halt steps in the Overview PDF, or book a flight.
3. **NYE-night stays** with free cancellation.

## Caveats

- Prices are researched estimates from Nov 2026, not live quotes. Seat availability could not be checked live (IRCTC needs login and captcha).
  Reddit was not reachable from the research environment, so traveller reports come from Team-BHP, Tripoto, travel blogs and local news.
- Train running days and timings sometimes conflict between sites. Each PDF marks these "verify". Confirm on IRCTC / NTES before paying.

## Rebuilding the PDFs

```bash
pip install reportlab   # uses DejaVu fonts from /usr/share/fonts/truetype/dejavu
python3 scripts/build_all.py            # all PDFs
python3 scripts/build_all.py plan3      # just one
```

Shared train, flight and gear tables are in `scripts/shared.py`; each plan's content is in `scripts/planN.py`.
