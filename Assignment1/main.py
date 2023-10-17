import A_star
import Map

def run_aStar():
    task = int(input("Skriv inn enten 1,2,3,4 for å kjøre task, trykk 5 for å avslutte "))
    while (task == 1 or task == 2 or task == 3 or task ==4 ):
        if(task == 1):
            map_obj = Map.Map_Obj(1)
            map_obj.show_map()
            A_stjerne = A_star.Astar(1)
            came_from = A_stjerne.a_star()
            temp_pos = list(came_from[tuple(map_obj.get_goal_pos())])
            while temp_pos != map_obj.get_start_pos():
                map_obj.replace_map_values(temp_pos, 5, map_obj.get_goal_pos())
                temp_pos = list(came_from[tuple(temp_pos)])
            map_obj.show_map()
        elif(task == 2):
            map_obj = Map.Map_Obj(2)
            map_obj.show_map()
            A_stjerne = A_star.Astar(2)
            came_from = A_stjerne.a_star()
            temp_pos = list(came_from[tuple(map_obj.get_goal_pos())])
            while temp_pos != map_obj.get_start_pos():
                map_obj.replace_map_values(temp_pos, 5, map_obj.get_goal_pos())
                temp_pos = list(came_from[tuple(temp_pos)])
            map_obj.show_map()
        elif(task == 3):
            map_obj = Map.Map_Obj(3)
            map_obj.show_map()
            A_stjerne = A_star.Astar(3)
            came_from = A_stjerne.a_star()
            temp_pos = list(came_from[tuple(map_obj.get_goal_pos())])
            while temp_pos != map_obj.get_start_pos():
                map_obj.replace_map_values(temp_pos, 5, map_obj.get_goal_pos())
                temp_pos = list(came_from[tuple(temp_pos)])
            map_obj.show_map()

        elif(task == 4):
            map_obj = Map.Map_Obj(4)
            map_obj.show_map()
            A_stjerne = A_star.Astar(4)
            came_from = A_stjerne.a_star()
            temp_pos = list(came_from[tuple(map_obj.get_goal_pos())])
            while temp_pos != map_obj.get_start_pos():
                map_obj.replace_map_values(temp_pos, 5, map_obj.get_goal_pos())
                temp_pos = list(came_from[tuple(temp_pos)])
            map_obj.show_map()

        else:
            break
        task = int(input("Skriv inn enten 1 eller 2 for å kjøre task 1/2, trykk enter for å avslutte "))
run_aStar()