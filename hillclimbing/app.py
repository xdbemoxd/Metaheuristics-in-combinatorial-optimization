import numpy as np

Vector = np.array( [ 6, 6, 2, 0, 1, 2, 6, 1 ] )

def cost( v : np.ndarray ) -> int :
    
    c = 0

    for i in range( v.size ) :

        for j in range( v.size ) :
            
            if i != j:
                
                if v[ i ] == v[ j ]:
                    
                    c += 1
                    
                elif v[ i ] - v[ j ] ==  i - j or v[ i ] - v[ j ] == j - i :
                
                    c += 1
    
    return c

def queen_cost( array_queen : np.ndarray, queen : int ) -> int:

    c = 0

    for j in range( array_queen.size ):
        
        if queen != j:

            if array_queen[ queen ] == array_queen[ j ]:
                    
                c += 1
                    
            elif array_queen[ queen ] - array_queen[ j ] ==  queen - j or array_queen[ queen ] - array_queen[ j ] == j - queen :
                
                c += 1
    
    return c


def generate_neighbor( house : np.ndarray ) -> np.ndarray :
    
    for i in range( house.size ):

        associated_cost = queen_cost( house, i )

        if associated_cost > 0:
            
            new_position = np.random.randint( 0, 8 )

            while new_position == house[ i ]:
                
                new_position = np.random.randint( 0, 8 )
            
            house[ i ] = new_position
    
    return house

var_cost = cost

print( "vector inicial:", Vector, "\nCosto:", var_cost( Vector ) )

def random_restart_hill_climbing_queen( ini_pos : np.ndarray, func_cost, max : int )  -> np.ndarray :
    
    time : int = 0
    set_time = np.random.randint( 1, 20, 10 )
    solution : np.ndarray = ini_pos.copy()
    best : np.ndarray = solution.copy()

    print( "vector de tiempos:", set_time )

    while ( time < max ) and ( func_cost( best ) != 0 )  :

        random_time = set_time[ np.random.randint( 0, 10 ) ]

        i = 0

        while i < random_time and func_cost( solution ) != 0 :
            
            neighbor = generate_neighbor( solution.copy() )

            if func_cost( neighbor ) < func_cost( solution ):

                solution = neighbor.copy()

            i += 1

        if func_cost( solution ) < func_cost( best ):

            best = solution.copy()

        time += 1

        solution = np.random.randint( 0, 8, 8 )

    return best

solution = random_restart_hill_climbing_queen( Vector, var_cost, 100 )

print( "Vector resultado: ", solution, "\nCosto asociado: ", var_cost( solution ) )