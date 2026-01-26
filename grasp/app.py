#Travelling Salesman Problem
import numpy as np
import sys
import random

array_size : int = 8;
alpha : float = 0.2

Vector = np.array( [ 6, 6, 2, 0, 1, 2, 6, 1 ] );

def queen_cost( array_queen : np.ndarray, queen : int ) -> int:

    c = 0;

    for j in range( array_queen.size ):
        
        if queen != j:

            if array_queen[ queen ] == array_queen[ j ]:
                    
                c += 1;
                    
            elif array_queen[ queen ] - array_queen[ j ] ==  queen - j or array_queen[ queen ] - array_queen[ j ] == j - queen :
                
                c += 1;
    
    return c;

def total_cost( house : np.ndarray ) -> int:

    temperature = 0;

    for i in range( house.size ):

        temperature += queen_cost( house, i ); 
    
    return temperature;

def generate_neighbor( house : np.ndarray ) -> np.ndarray :
    
    for i in range( house.size ):

        associated_cost = queen_cost( house, i );

        if associated_cost > 0:
            
            new_position = np.random.randint( 0, 8 );

            while new_position == house[ i ]:
                
                new_position = np.random.randint( 0, 8 );
            
            house[ i ] = new_position;
    
    return house;

def initialize_candidate_list( array_queen : np.array, candidate_choice : list ) -> list :
    
    neighbors = [];
    current_neighbor = np.array;
    times : int = 50;

    while ( times > 0 ):
        
        current_neighbor = generate_neighbor( array_queen.copy() );

        if not any( np.array_equal( current_neighbor, n ) for n in neighbors ):

            neighbors.append( current_neighbor );

        times -= 1;
    
    return neighbors;
 
def build_rcl( current_candidates : list, a : float ) -> list :

    min_cost : float = sys.float_info.max;
    max_cost : float = sys.float_info.min;
    cost : float = 0
    aux = []

    for i in current_candidates:
        
        cost_aux = total_cost( i );

        if cost_aux > max_cost:

            max_cost = cost_aux;

        if cost_aux < min_cost:

            min_cost = cost_aux;
    
    cost = min_cost + ( a * ( max_cost - min_cost ) );

    for i in current_candidates:

        if total_cost( i ) <= cost:
            
            aux.append( i );

    return aux;


def build_initial_solution( array_queen : np.array ) -> list :
    
    x = [];
    c = [];
    aux = [];
    s = np.empty( array_size );

    c = initialize_candidate_list( array_queen, x );

    rcl = build_rcl( c, alpha );

    s = random.choice( rcl );

    return s;

def local_search( s_0 : np.array ) -> np.array:
    
    s_l : np.array2 = s_0.copy();
    band : bool = False;
    s = np.empty( array_size );

    while( not band ):
        band = True
        
        s = generate_neighbor( s_l ); 

        if total_cost( s_l ) > total_cost( s ):
            s_l = s;
            band = False
    
    return s_l


def grasp_n_queen( array_queen : np.array ) -> np.array :
    
    cost : float = sys.float_info.max;
    times : int = 50;
    optimal_solution : np.array = array_queen.copy();
    solution = list;
    local_solution = list;

    while( times > 0 and total_cost( optimal_solution ) != 0 ):

        solution = build_initial_solution( array_queen );
        local_solution = local_search( solution.copy() );

        if total_cost(optimal_solution) > total_cost(local_solution):
            optimal_solution = local_solution

        times-=1; 

    return optimal_solution;

    

#print( matrix[ 0 ] );

solution = grasp_n_queen( Vector );

print( solution )
print( total_cost( solution ) )



