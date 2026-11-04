"""Section builders that several plan PDFs reuse."""
import shared as S

ONWARD_W = [0.17, 0.21, 0.15, 0.08, 0.17, 0.22]
RETURN_W = [0.2, 0.17, 0.18, 0.09, 0.14, 0.22]
FLIGHT_W = [0.18, 0.24, 0.12, 0.26, 0.2]
DK_W = [0.16, 0.2, 0.2, 0.11, 0.18, 0.15]


def pick(table, idx):
    return [table[0]] + [table[i] for i in idx]


def onward(d, idx=(1, 2, 3, 4, 5), title="Hyderabad → Delhi on 24 Dec: board in Hyderabad, Kazipet, Warangal or Vijayawada"):
    d.h2(title)
    d.table(pick(S.ONWARD_TRAINS, idx), ONWARD_W)
    d.small(S.TO_KAZIPET)
    d.space(2)
    d.small(S.TELANGANA_HALTS)
    d.space(4)
    d.callout("Waitlisted? Check every station and halt this way", S.HALT_METHOD + [S.PNR_NOTE], "warn")


def returns(d, idx=(1, 2, 3, 4)):
    d.h2("Back to Hyderabad by 3 Jan")
    d.table(pick(S.RETURN_TRAINS, idx), RETURN_W)


def delhi_trains(d, onward_idx=(1, 2, 3, 4, 5), return_idx=(1, 2, 3, 4)):
    onward(d, onward_idx)
    returns(d, return_idx)


def delhi_day(d):
    d.callout("The Delhi gap: use it, don't waste it", S.HELPFUL_DELHI_DAY, "info")


def kalka_toy_train(d, show_return=False):
    d.h2("Delhi → Kalka → Shimla by toy train (connections and buffers)")
    d.table(S.DELHI_KALKA, DK_W)
    d.small(S.DELHI_KALKA_NOTE)
    d.space(3)
    d.h2("Kalka–Shimla toy train timetable" + (" (both directions)" if show_return else ""))
    rows = S.TOY_TRAIN if show_return else S.TOY_TRAIN[:6]
    d.table(rows, [0.11, 0.19, 0.13, 0.13, 0.2, 0.24])
    d.small(S.TOY_NOTE)
    d.space(4)


def flights(d, idx, title="Flights from Hyderabad (to save 1–2 days)"):
    d.h2(title)
    d.table(pick(S.FLIGHTS, idx), FLIGHT_W)
    d.small(S.FLIGHT_NOTE)
    d.space(4)


def vehicles(d):
    d.h2("Getting around as 6")
    d.table(S.VEHICLES, [0.2, 0.14, 0.3, 0.14, 0.22])


def airbnb(d, rows):
    """rows: [nights, where, best-rated pick, budget pick, est ₹/night for 6]. Per-person column is computed."""
    d.h1("Where you sleep: Airbnb picks for 6 (best-rated and budget)")
    out = [["Nights", "Area", "Best-rated pick", "Budget pick", "Est. Dec price, 6 people / night", "≈ per person / night"]]
    for nights, where, best, budget, (lo, hi) in rows:
        pp = f"₹{round(lo / 6 / 50) * 50:,}–{round(hi / 6 / 50) * 50:,}"
        out.append([nights, where, best, budget, f"₹{lo:,}–{hi:,}", pp])
    d.table(out, [0.09, 0.11, 0.28, 0.24, 0.14, 0.14])
    d.small(S.AIRBNB_NOTE)
    d.space(3)
    d.callout("How to pick the best-rated vs the cheapest on Airbnb", S.AIRBNB_HOWTO, "info")


def gear(d, local_rows):
    d.h1("Winter gear: what to buy, what to rent, and where")
    d.p(S.GEAR_SUMMARY)
    d.table(pick(S.GEAR_TABLE, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)), [0.2, 0.1, 0.2, 0.3, 0.2])
    d.h2("Rental points on this route")
    d.table(local_rows, [0.25, 0.45, 0.3])


def packing_and_safety(d, extra_safety=()):
    d.h2("Carry list")
    d.bullets(S.PACKING)
    d.h2("Safety &amp; buffers")
    d.bullets(list(S.COMMON_SAFETY) + list(extra_safety))
