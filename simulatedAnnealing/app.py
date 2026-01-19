import numpy as np

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

def generate_neighbor( house : np.ndarray ) -> np.ndarray :
    
    for i in range( house.size ):

        associated_cost = queen_cost( house, i );

        if associated_cost > 0:
            
            new_position = np.random.randint( 0, 8 );

            while new_position == house[ i ]:
                
                new_position = np.random.randint( 0, 8 );
            
            house[ i ] = new_position;
    
    return house;

def total_cost( house : np.ndarray ) -> int:

    temperature = 0;

    for i in range( house.size ):

        temperature += queen_cost( house, i ); 
    
    return temperature;

def probability_function( solution_status : np.ndarray ) -> float :

    EPSILON = 1e-9

    number = np.log( 1 + solution_status.var() ) / np.log( 2 );
    
    res = solution_status[ 0 ] / ( 1 + ( solution_status[ 0 ] * ( number ) ) / ( 3 * solution_status.std() + EPSILON ) );

    return res;

def simulated_annealing_queen( ini_pos : np.ndarray ) -> np.ndarray:

    temperature = total_cost( ini_pos );
    solution : np.ndarray = ini_pos.copy();
    solution_status = np.zeros( 2, dtype = int );
    time : int = 20;
    global_time : int = 500

    while( total_cost( solution ) != 0 and global_time > 1 ):

        solution_status[ 0 ] = temperature;

        while( time != 0 ):

            neighbor = generate_neighbor( solution.copy() );

            solution_status[ 1 ] = total_cost( neighbor );

            if solution_status[ 1 ] - solution_status[ 0 ] < 0:

                solution = neighbor.copy();

                temperature = solution_status[ 1 ];
            
            else:

                number_between_0_1 = np.random.rand();

                if number_between_0_1 < probability_function( solution_status ):
                    
                    solution = neighbor.copy();

                    temperature = solution_status[ 1 ];

            time -= 1;
        
        global_time -= 1;
    
    return solution;


print( "solucion inicial: ", Vector, " costo asociado: ", total_cost( Vector ) );

solution = simulated_annealing_queen( Vector );

cost = total_cost( solution );

print( "Solucion encontrada: ", solution, " costo asociado: ", cost );














