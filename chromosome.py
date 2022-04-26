import random as r
import numpy as np


def convert_dec_to_bin(number):
    return int(bin(number)[2:])


class Chromosome:
    def __init__(self):
        self.chromosome = np.uint8(r.randint(0, 255))

    def get_chromosome(self):
        return self.chromosome

    def get_binary(self):
        return convert_dec_to_bin(self.chromosome)

    def set_chromosome(self, new: np.uint8):
        self.chromosome = new

    def set_binary(self, bit_position):
        self.chromosome |= (1 << bit_position)

    def clear_binary(self, bit_position):
        self.chromosome &= ~(1 << bit_position)

    def toggle_binary(self, bit_position):
        self.chromosome ^= (1 << bit_position)

    def locus_swap(self, locus_position, chromosome_to_swap):
        for i in range(locus_position):
            gene1 = self.get_bit(i)
            gene2 = chromosome_to_swap.get_bit(i)
            if gene1 != gene2:
                self.toggle_binary(i)
                chromosome_to_swap.toggle_binary(i)

    def get_bit(self, bit_position):
        return (self.chromosome >> bit_position) & 1

    def print_binary(self):
        print(format(self.chromosome, '08b'))
