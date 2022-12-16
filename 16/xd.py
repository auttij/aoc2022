Fs = {}
Vs = {}
Os = {}

IN = open('16/input2.txt').read()
Fs = {}
Vs = {}
Os = {}

for ln in IN.split("\n"):
    A, B = ln.split("; ")
    _, name, *_, rate = A.split()
    rate = int(rate[5:])
    valves = B.split("valve")[1]
    if valves.startswith("s "):
        valves = valves[2:]
    valves = valves.strip().split(", ")
    
    Fs[name] = rate
    Vs[name] = valves
    Os[name] = False

# _seen = {}
# m = 0
# def f(t, pos, flow):
#     global m, Vs, Os, _seen
    
#     if _seen.get((t, pos), -1) >= sum(flow):
#         return
#     _seen[t, pos] = sum(flow)
    
#     #
#     if t == 30:
#         m = max(m, sum(flow))
#         print(m)
#         return
    
#     # Open valve here?
#     for k in (0, 1):
#         if k == 0:
#             if Os[pos] or Fs[pos] <= 0:
#                 continue
                
#             Os[pos] = True
#             j = sum(Fs[k] for k, v in Os.items() if v)
#             f(
#                 t + 1,
#                 pos,
#                 flow + [ j ]
#             )
#             Os[pos] = False
#         else:
#             j = sum(Fs[k] for k, v in Os.items() if v)
#             for v in Vs[pos]:
#                 f(
#                     t + 1,
#                     v if v is not None else pos,
#                     flow + [ j ]
#                 )

# f(1, "AA", [ 0 ])

_seen = {}
m = 0
def f(t, pos1, pos2, flow):
    global m, Vs, Os, _seen, _seen2
    
    if _seen.get((t, pos1, pos2), -1) >= sum(flow):
        return
    _seen[t, pos1, pos2] = sum(flow)
    
    if t == 26:
        if sum(flow) > m:
            m = sum(flow)
            print(m, flow)
        return
    
    # all open? just stay put...
    if all(v for k, v in Os.items() if Fs[k] > 0):
        tf = sum(Fs[k] for k, v in Os.items() if v)
        f(t + 1, pos1, pos2, flow + [tf])
        return
    
    # possible options for us...
    for k in (0, 1):
        if k == 0:
            if Os[pos1] or Fs[pos1] <= 0:
                continue
                
            Os[pos1] = True
            
            for k2 in (0, 1):
                if k2 == 0:
                    if Os[pos2] or Fs[pos2] <= 0:
                        continue
                    
                    Os[pos2] = True
                    j = sum(Fs[k] for k, v in Os.items() if v)
                    f(
                        t + 1,
                        pos1,
                        pos2,
                        flow + [ j ]
                    )
                    Os[pos2] = False
                else:
                    j = sum(Fs[k] for k, v in Os.items() if v)
                    for v2 in Vs[pos2]:
                        f(
                            t + 1,
                            pos1,
                            v2,
                            flow + [ j ]
                        )
            Os[pos1] = False
        else:
            j = sum(Fs[k] for k, v in Os.items() if v)
            for v in Vs[pos1]:
                for k2 in (0, 1):
                    if k2 == 0:
                        if Os[pos2] or Fs[pos2] <= 0:
                            continue

                        Os[pos2] = True
                        j = sum(Fs[k] for k, v in Os.items() if v)
                        f(
                            t + 1,
                            v,
                            pos2,
                            flow + [ j ]
                        )
                        Os[pos2] = False
                    else:
                        j = sum(Fs[k] for k, v in Os.items() if v)
                        for v2 in Vs[pos2]:
                            f(
                                t + 1,
                                v,
                                v2,
                                flow + [ j ]
                            )

f(1, "AA", "AA", [ 0 ])