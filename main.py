from pathlib import Path

# One dad joke, told out loud by a father at the table. Judge criteria,
# in order: (1) a dad joke a father would tell, (2) the pun lands cleanly
# on first read, (3) fresh rather than a thousand-times-told classic,
# (4) tight with the punchline at the end, (5) natural spoken rhythm.
# The turn is a single clean pun ("waves ... waves back") inside a
# father-son exchange, so the setup sounds spoken and the groan lands
# on the last words. Revision 2: "and" -> "but" with a comma instead of
# the em-dash — the contrast word gives the punchline its beat, and the
# comma reads more naturally aloud than the dash. Domain (the ocean)
# avoids the over-told classics (scarecrow, bicycle, tomato, stairs)
# and the other entrants' topics seen on the board (bread, suitcases,
# chemistry, salad, Wi-Fi).
JOKE = (
    "I asked Dad why the ocean is so salty. He said, 'Because it waves "
    "at everyone, but nobody ever waves back.'"
)

# Self-check the gate before writing: 1-200 characters, not only whitespace.
if len(JOKE) < 1 or len(JOKE) > 200 or JOKE.strip() == "":
    raise SystemExit(f"joke is {len(JOKE)} characters, outside the 1-200 gate")

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE, encoding="utf-8")
