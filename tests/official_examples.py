import re, json, sys, inspect, importlib, ast
sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "solutions"))
src = open(__import__("os").path.join(__import__("os").path.dirname(__file__), "subjects_data.js")).read()
# each subject: name, signature, examples (JSON-ish), forbidden
subs = re.split(r"\n  \{\n    id: ", src)[1:]
bad = 0; total = 0
for s in subs:
    name = re.search(r'name: "([^"]+)"', s)[1]
    sig = re.search(r'signature: "([^"]+)"', s)[1]
    ex = re.search(r"examples: (\[.*?\n      \])", s, re.S)[1]
    exs = json.loads(ex)
    forb = re.search(r"forbidden: (\[[^\]]*\])", s)
    SITE = {"py_room_scheduler": "py_room_scheduler_site_format"}  # site shows the pre-exam return format
    mod = importlib.import_module(SITE.get(name, name))
    fname = re.match(r"def (\w+)\(", sig)[1]
    fn = getattr(mod, fname + ("_site_format" if name in SITE else ""))
    # signature must match exactly (param names + annotations)
    want = ast.parse(sig + " pass").body[0]
    got = inspect.signature(fn)
    assert [a.arg for a in want.args.args] == list(got.parameters), (name, got)
    print(f"{name}: signature OK  {sig}")
    env = {n: getattr(mod, n) for n in dir(mod) if not n.startswith("_")}
    if name in SITE: env[fname] = fn
    for e in exs:
        total += 1
        res = eval(e["input"], env); exp = eval(e["output"], env)
        ok = res == exp and type(res) is type(exp)
        bad += not ok
        print("   ", "OK " if ok else "BAD", e["input"][:70], "->", repr(res)[:60])
    if forb: print("    forbidden:", forb[1])
print("examples:", total, "failures:", bad)
