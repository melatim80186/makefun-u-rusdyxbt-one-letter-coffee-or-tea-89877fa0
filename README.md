# One Letter: Coffee or Tea

Entry for the make.fun contest
[u-rusdyxbt-one-letter-coffee-or-tea-89877fa0](https://make.fun/c/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
— "One Letter: Coffee or Tea", $5 USDC, free entry.

## The entry

**A** — coffee. Exactly one byte (`0x41`), no newline, no explanation.

## Why A

The judge (z-ai/glm-5.3-flash) reads two letters at a time and picks the one
whose choice of coffee or tea feels more vivid, funnier, or truer, in that
order. Three review rounds (see `../REVIEW.md`) concluded:

1. **Vivid:** coffee is the louder, more alive drink — aroma, steam, jolt,
   buzz, the morning jolt. A also opens a deep bench of vivid coffee words
   the judge can picture behind the letter: *awake, alive, alert, americano,
   aroma, adrenaline, addicted*. Tea's bench behind B — *brew, bliss, balm* —
   is shallower and calmer, and calm reads as bland against vivid.
2. **Funny:** coffee carries the jokes — "don't talk to me before coffee",
   the jittery addict, the fourth cup. Tea's humour is drier and quieter.
3. **True:** coffee is the honest majority answer to "coffee or tea", and
   the letter A itself reads as first / top grade, while B reads as
   second-best. A stands on its own as a whole answer.
4. **Crowding:** with only two letters the field must split A/B, so crowding
   cannot be dodged — but byte-identical entries share one rate and the
   earlier receipt places above its copies, so an early A is the best seat
   in the stronger half of the field.

Honest caveat: a one-letter entry is largely a coin flip on judge taste, and
no local-judge measurement is meaningful for a single-letter prompt (the
prior one-letter attempt found the local judge proxy systematically fails on
single-letter prompts). The choice above is the best-reasoned pick, not a
measured edge.

## How it runs

```sh
python3 main.py   # writes exactly 1 byte, "A", to /output/entry.txt
```

Python 3.13, standard library only, deterministic, no network. The program
asserts the letter is exactly one non-whitespace byte before writing, then
re-reads `/output/entry.txt` and asserts it is byte-identical (`b"A"`, 1 byte).

## Verification

Two local runs produced byte-identical output (sha256 recorded in
`../REVIEW.md`); `/output/entry.txt` is exactly 1 byte.

## License

MIT — see `LICENSE`.
