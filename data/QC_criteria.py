# QC criteria for Aggregat QC steps
QC_criteria = {
    'Illumina TruSeq PCR-free': {
        'Covaris 180bp': {
            'Concentration': (20, 750),
            'Volume (ul)': 10,
            'Amount (ng)': 1000
        },
        'Covaris 350bp': {
            'Concentration': (20, 750),
            'Volume (ul)': 10,
            'Amount (ng)': 1000
        },
        'Covaris 670bp': {
            'Concentration': (40, 750),
            'Volume (ul)': 10,
            'Amount (ng)': 2200
        },
    },
    'SMARTer ThruPLEX DNA-seq (complex genome, metagenomes)': {
        'default': {
            'Concentration': (1, 75),
            'Volume (ul)': 10,
            'Amount (ng)': 10
        }
    },
    'SMARTer ThruPLEX DNA-seq (small genome)': {
        'default': {
            'Concentration': (0.2, 75),
            'Volume (ul)': 10,
            'Amount (ng)': 1
        }
    },
    'SMARTer ThruPLEX DNA-seq (ChIP)': {
        'default': {
            'Concentration': (0.2, 75),
            'Volume (ul)': 10,
            'Amount (ng)': 0.1
        }
    },
    'SMARTer ThruPLEX DNA-seq (FFPE)': {
        'default': {
            'Concentration': (10, 50),
            'Volume (ul)': 10,
            'Amount (ng)': 100
        }
    },
    'RAD-seq': {
        'default': {
            'Concentration': (15.4, 100),
            'Volume (ul)': 15,
            'Amount (ng)': 200
        }
    },
    'Illumina TruSeq Stranded mRNA (polyA)': {
        'default': {
            'Concentration': (4, 500),
            'Volume (ul)': 10,
            'Amount (ng)': 200,
            'RIN': 8
        }
    },
    'Illumina TruSeq Stranded total RNA': {
        'default': {
            'Concentration': (50, 500),
            'Volume (ul)': 15,
            'Amount (ng)': 500,
            'RIN': 8
        },
        'No selection': {
            'Concentration': (10, 25),
            'Volume (ul)': 10,
            'Amount (ng)': 50,
            'RIN': 8
        },
        'No depletion': {
            'Concentration': (10, 25),
            'Volume (ul)': 10,
            'Amount (ng)': 50,
            'RIN': 8
        }
    },
    'Illumina TruSeq small RNA': {
        'default': {
            'Concentration': (200, 500),
            'Volume (ul)': 10,
            'Amount (ng)': 1000,
        }
    },
    'SMARTer Total Stranded RNA-seq, Pico input mammalian': {
        'default': {
            'Concentration': (1.25, 25),
            'Volume (ul)': 10,
            'Amount (ng)': 10,
            'RIN': 8,
            'DV200': 30
        },
        'No fragmentation': {
            'Concentration': (1.25, 25),
            'Volume (ul)': 10,
            'Amount (ng)': 10,
            'RIN': 8,
            'DV200': 30
        }
    },
    'Finished library (by user)': {
        'MiSeq':{
            'default': {
                'default': {
                    'Concentration': 2,
                    'Volume (ul)': 15,
                }
            }
        },
        'NovaSeq 6000': {
            'SP': {
                'onboard clustering': {
                    'Concentration': 2,
                    'Volume (ul)': 110,
                },
                'XP clustering': {
                    'Concentration': 1.5,
                    'Volume (ul)': 25,
                }
            },
            'S1': {
                'onboard clustering': {
                    'Concentration': 2,
                    'Volume (ul)': 110,
                },
                'XP clustering':{
                    'Concentration': 1.5,
                    'Volume (ul)': 25,
                }
            },
            'S2': {
                'onboard clustering': {
                    'Concentration': 2,
                    'Volume (ul)': 160,
                },
                'XP clustering':{
                    'Concentration': 1.5,
                    'Volume (ul)': 30,
                }
            },
            'S4': {
                'onboard clustering': {
                    'Concentration': 2,
                    'Volume (ul)': 320,
                },
                'XP clustering':{
                    'Concentration': 1.5,
                    'Volume (ul)': 35,
                }
            }
        },
        'NextSeq 2000': {
            'P2': {
                'default': {
                    'Concentration': 2,
                    'Volume (ul)': 15,
                }
            },
            'P3': {
                'default': {
                    'Concentration': 2,
                    'Volume (ul)': 15,
                }
            }
        }
    }
}
