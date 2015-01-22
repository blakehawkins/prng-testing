
#include <cstdlib>
#include <iostream>

#include <boost/lexical_cast.hpp>

#include "main.hpp"
#include "clcg_rnd_gen.hpp"
#include "cmt_rand_int32.hpp"

int main(int argc, char** arvs)
{
    // uint32 seed1 = MT.Random();
    // uint32 seed2 = MT.Random();

    // for (samples) { 
    //      uint32 seed=MT.Random(); 
    //      LCG rng1(seed1 ^ seed);
    //      LCG rng2(seed2 ^ seed); 
    //      [test results of rng1 vs rng2] }
    //      with iterations for different seed1 & 2 also
    CLCGRndGen n;
    CMTRand_int32 o;

    std::cout << boost::lexical_cast<unsigned long>(n.GenerateUint32()) << 
            std::endl << boost::lexical_cast<unsigned long>(o.GenerateUint32()) 
            << std::endl;

    std::cout << boost::lexical_cast<unsigned long>(n.GenerateUint32()) << 
            std::endl << boost::lexical_cast<unsigned long>(o.GenerateUint32()) 
            << std::endl;

    std::cout << boost::lexical_cast<unsigned long>(n.GenerateUint32()) << 
            std::endl << boost::lexical_cast<unsigned long>(o.GenerateUint32()) 
            << std::endl;

    std::cout << boost::lexical_cast<unsigned long>(n.GenerateUint32()) << 
            std::endl << boost::lexical_cast<unsigned long>(o.GenerateUint32()) 
            << std::endl;

    return 0;
}
