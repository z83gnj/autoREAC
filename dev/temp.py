reactionForce = {
    # filename : {time : {node : {f_x: 0, fy: 0, fz: 0}}
    # filename : {time : {node : [val1, val2, val3, ....]}} --> testing??? w/ list
}
# TODO Test valami
reactionForce["test1"] = {
    0.1 : {"fx":1.1, "fy": 2.1, "fz":3.1}, 
#    0.2 : {"fx":4.1, "fy": 5.1, "fz":6.1}, 
#    0.3 : {"fx":7.1, "fy": 8.1, "fz":9.1},
    }
print(reactionForce["test1"].keys())

reactionForce["test1"].update({0.2 : {"fx":4.1, "fy": 5.1, "fz":6.1}})
#reactionForce["test1"] = 
#   0.1 : {"fx":1.1, "fy": 2.1, "fz":3.1}, 
#    0.2 : {"fx":4.1, "fy": 5.1, "fz":6.1}, 
#    0.3 : {"fx":7.1, "fy": 8.1, "fz":9.1},
#    }

print(reactionForce["test1"].keys())



#print(reactionForce.keys())
#print(reactionForce["test1"].keys())
#print(reactionForce.values())


#print(reactionForce[0.1]["fx"],type(reactionForce[0.1]["fx"]))

#reactionForce[0.1]["fx"] += 125.12

#print(reactionForce[0.1]["fx"],type(reactionForce[0.1]["fx"]))

#for key in reactionForce.keys():
 #   print(reactionForce[key][0.1]["fx"],reactionForce[key][0.1]["fy"],reactionForce[key][0.1]["fz"])