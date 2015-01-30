
#include <cstdlib>
#include <iostream>

#include <boost/lexical_cast.hpp>

#include "main.hpp"
#include "clcg_rnd_gen.hpp"
#include "cmt_rand_int32.hpp"

using namespace std;

const int NUM_TESTS        = 1;
const int NUM_PUBLIC_SEEDS = 10;
const int NUM_SAMPLES      = 100;

// NUM_TESTS times, generate NUM_PUBLIC_SEEDS seeds and two static seeds with 
// MT, xor them together and use the result NUM_SAMPLES times to produce random
// values with a CLCG generator. Print the pairs side by side.

// Later, a python script will calculate the cross-correlation between the CLCG
// sets generated with shared public seeds.
int main(int argc, char** arvs)
{
    CMTRand_int32 mt_gen;

    for(int i = 0; i < NUM_TESTS; i++)
    {
        uint32 static_seed_a = mt_gen.GenerateUint32();
        uint32 static_seed_b = mt_gen.GenerateUint32();
        cout    << endl 
                << "\tStatic Seeds: [" 
                << boost::lexical_cast<unsigned long>(static_seed_a)
                << ", "
                << boost::lexical_cast<unsigned long>(static_seed_b)
                << "]"
                << endl;

        for(int j = 0; j < NUM_PUBLIC_SEEDS; j++)
        {
            uint32 public_seed = mt_gen.GenerateUint32();
            CLCGRndGen remote_gen_a(static_seed_a ^ public_seed);
            CLCGRndGen remote_gen_b(static_seed_b ^ public_seed);

            cout    << "[" 
                    << boost::lexical_cast<unsigned long>(public_seed) 
                    << "\t^\t" 
                    << boost::lexical_cast<unsigned long>(static_seed_a) 
                    << "]\t";

            for(int k = 0; k < NUM_SAMPLES; k++)
            {
                cout    << boost::lexical_cast<uint32>(remote_gen_a.GenerateUint32())
                        << "\t";
            }

            cout    << endl 
                    << "[" 
                    << boost::lexical_cast<unsigned long>(public_seed) 
                    << "\t^\t" 
                    << boost::lexical_cast<unsigned long>(static_seed_b) 
                    << "]\t";

            for(int k = 0; k < NUM_SAMPLES; k++)
            {
                cout    << boost::lexical_cast<uint32>(remote_gen_b.GenerateUint32())
                        << "\t";
            }

            cout << endl;
        }
    }

    return 0;
}
