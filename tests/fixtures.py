import pytest
import pandas as pd


@pytest.fixture(scope="session")
def create_testfolder(tmp_path_factory):
    """Create test folder."""
    fn = tmp_path_factory.mktemp("testfolder")
    return (fn)


@pytest.fixture
def database_paths():
    """Database paths for tests."""
    db = {
        'igblast_db': "database/igblast/",
        'germline': "database/germlines/imgt/human/vdj/",
        'blastdb': "database/blast/human/",
        'blastdb_fasta': "database/blast/human/human_BCR_C.fasta",
    }
    return (db)


@pytest.fixture
def processed_files():
    """Database paths for tests."""
    fl = {
        'filtered': "filtered_contig_igblast_db-pass_genotyped.tsv",
        'all': "all_contig_igblast_db-pass_genotyped.tsv",
    }
    return (fl)


@pytest.fixture
def fasta_10x():
    """Standard cellranger fasta file to test the preprocessing."""
    seq = {
        'AAACCTGTCATATCGG-1_contig_1':
        'TGGGGAGGAGTCAGTCCCAACCAGGACACGGCCTGGACATGAGGGTCCCTGCTCAGCTCCTGGGGCTCCTGCTGCTCTGGCTCTCAGGTGCCAGATGTGACATCCAGATGACCCAGTCTCCATCCTCCCTGTCTGCATCTGTGGGAGACAGAGTCACCATCACTTGCCAGGCGACACAAGACATTAACAATTATGTAAATTGGTATCAGCAGAAACCAGGGAAAGCCCCTAAACTCCTGATCTACGATGCATTGAATTTAGAAATAGGGGTCCCATCAAGATTCAGTGGAAGAGGGTCTGGGACAGTCTTTATTCTCACCATCAGCAGCCTGCAGCCTGAAGATGTTGCAACATACTACTGTCAACAATATGACGAACTTCCCGTCACTTTCGGCGGAGGGACCAATGTGGAAATGAGACGAACTGTGGCTGCACCATCTGTCTTCATCTTCCCGCCATCTGATGAGCAGTTGAAATCTGGAACTGCCTCTGTTGTGTGCCTGCTGAATAACTTCTATCCCAGAGAGGCCAAAGTACAGTGGAAGGTGGATAACGC',
        'AAACCTGTCCGTTGTC-1_contig_1':
        'AGGAGTCAGACCCTGTCAGGACACAGCATAGACATGAGGGTCCCCGCTCAGCTCCTGGGGCTCCTGCTGCTCTGGCTCCCAGGTGCCAGATGTGCCATCCGGATGACCCAGTCTCCATCCTCATTCTCTGCATCTACAGGAGACAGAGTCACCATCACTTGTCGGGCGAGTCAGGGTATTAGCAGTTATTTAGCCTGGTATCAGCAAAAACCAGGGAAAGCCCCTAAGCTCCTGATCTATGCTGCATCCACTTTGCAAAGTGGGGTCCCATCAAGGTTCAGCGGCAGTGGATCTGGGACAGATTTCACTCTCACCATCAGCTGCCTGCAGTCTGAAGATTTTGCAACTTATTACTGTCAACAGTATTATAGTTACCCTCGGACGTTCGGCCAAGGGACCAAGGTGGAAATCAAACGAACTGTGGCTGCACCATCTGTCTTCATCTTCCCGCCATCTGATGAGCAGTTGAAATCTGGAACTGCCTCTGTTGTGTGCCTGCTGAATAACTTCTATCCCAGAGAGGCCAAAGTACAGTGGAAGGTGGATAACGC',
        'AAACCTGTCCGTTGTC-1_contig_2':
        'ATCACATAACAACCACATTCCTCCTCTAAAGAAGCCCCTGGGAGCACAGCTCATCACCATGGACTGGACCTGGAGGTTCCTCTTTGTGGTGGCAGCAGCTACAGGTGTCCAGTCCCAGGTGCAGCTGGTGCAGTCTGGGGCTGAGGTGAAGAAGCCTGGGTCCTCGGTGAAGGTCTCCTGCAAGGCTTCTGGAGGCACCTTCAGCAGCTATGCTATCAGCTGGGTGCGACAGGCCCCTGGACAAGGGCTTGAGTGGATGGGAGGGATCATCCCTATCTTTGGTACAGCAAACTACGCACAGAAGTTCCAGGGCAGAGTCACGATTACCGCGGACGAATCCACGAGCACAGCCTACATGGAGCTGAGCAGCCTGAGATCTGAGGACACGGCCGTGTATTACTGTGCGACTACGTATTACTATGATAGTAGTGGTTATTACCAGAATGATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
        'AAACCTGTCGAGAACG-1_contig_1':
        'ACTGTGGGGGTAAGAGGTTGTGTCCACCATGGCCTGGACTCCTCTCCTCCTCCTGTTCCTCTCTCACTGCACAGGTTCCCTCTCGCAGGCTGTGCTGACTCAGCCGTCTTCCCTCTCTGCATCTCCTGGAGCATCAGGCAGGCTCACCTGCACCTTACGCAGTGACATCAATGTTGGTACGTACAGGATATATTGGTACCAGCGGAAGCCAGGGAGTCCTCCCCAGTATCTCCTGAGGTACAAATCAGACTCAGATAAGCAGCAGGGCTCTGGAGTCCCCAGCCGCTTCTCTGGATCCAAAGATGCTTCGGCCAATGCAGGGATTTTACTCATCTCTGGGCTCCAGTCTGAGGATGAGGCTGACTATTATTGTATGATTTGGCACAGCAGCGCTTGGGTGGTCGGCGGAGGGACCAAGCTGACCGTCCTAGGTCAGCCCAAGGCTGCCCCCTCGGTCACTCTGTTCCCACCCTCCTCTGAGGAGCTTCAAGCCAACAAGGCCACACTGGTGTGTCTCATAAGTGACTTCTACCCGGGAGCCGTGACAGTGGCCTGGAAGGCAGATAGCAGCCCCGTCAAGGCGGGAGTGGAGACCACCACACCCTCCAAACAAAGCAACAACAAGTACGCGGCCAGCAGCTA',
        'AAACCTGTCGAGAACG-1_contig_2':
        'GGGAGCATCACCCAGCAACCACATCTGTCCTCTAGAGAATCCCCTGAGAGCTCCGTTCCTCACCATGGACTGGACCTGGAGGATCCTCTTCTTGGTGGCAGCAGCCACAGGAGCCCACTCGCAGGTGCAACTGGTGCAGTCTGGGGGTGAGGTAAAGAAGCCTGGGGCCTCAGTGAAGGTCTCCTGCAAGGCTTCTGGATACACCTTCACCGACTACTTCATACAGTGGCTGCGACACGCCCCTGGACAGGGGCTTGATTGGATGGGTTTAATCAACCCTAACAGTGGTGACACCAACTATGCACAGAAGTTTCAGGGCAGAGTCACCATGACCAGGGACACGTCCATCAGTACAGCCTACATGGAACTGAGCAGCCTGAGATCTGACGACACGGCCGTATATTACTGTGCGAGAGAGATAGAGGGGGACGGTGTTTTTGAAATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
        'AAACCTGTCTTGAGAC-1_contig_1':
        'AGGAGTCAGACCCAGTCAGGACACAGCATGGACATGAGGGTCCCCGCTCAGCTCCTGGGGCTCCTGCTGCTCTGGCTCCCAGGTGCCAGATGTGTCATCTGGATGACCCAGTCTCCATCCTTACTCTCTGCATCTACAGGAGACAGAGTCACCATCAGTTGTCGGATGAGTCAGGGCATTAGCAGTTATTTAGCCTGGTATCAGCAAAAACCAGGGAAAGCCCCTGAGCTCCTGATCTATGCTGCATCCACTTTGCAAAGTGGGGTCCCATCAAGGTTCAGTGGCAGTGGATCTGGGACAGATTTCACTCTCACCATCAGTTGCCTGCAGTCTGAAGATTTTGCAACTTATTACTGTCAACAGTATTATAGTTTCCCGTACACTTTTGGCCAGGGGACCAAGCTGGAGATCAAACGAACTGTGGCTGCACCATCTGTCTTCATCTTCCCGCCATCTGATGAGCAGTTGAAATCTGGAACTGCCTCTGTTGTGTGCCTGCTGAATAACTTCTATCCCAGAGAGGCCAAAGTACAGTGGAAGGTGGATAACGC',
        'AAACCTGTCTTGAGAC-1_contig_2':
        'GGAGTCTCCCTCACCGCCCAGCTGGGATCTCAGGGCTTCATTTTCTGTCCTCCACCATCATGGGGTCAACCGCCATCCTCGCCCTCCTCCTGGCTGTTCTCCAAGGAGTCTGTGCCGAGGTGCAGCTGGTGCAGTCTGGAGCAGAGGTGAAAAAGCCGGGGGAGTCTCTGAAGATCTCCTGTAAGGGTTCTGGATACAGCTTTACCAGCTACTGGATCGGCTGGGTGCGCCAGATGCCCGGGAAAGGCCTGGAGTGGATGGGGATCATCTATCCTGGTGACTCTGATACCAGATACAGCCCGTCCTTCCAAGGCCAGGTCACCATCTCAGCCGACAAGTCCATCAGCACCGCCTACCTGCAGTGGAGCAGCCTGAAGGCCTCGGACACCGCCATGTATTACTGTGCGAGACATATCCGTGGGAACAGATTTGGCAATGATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
        'AAACGGGAGCGACGTA-1_contig_1':
        'GGGGACTTTCTGAGACTCATGGACCTCCTGCACAAGAACATGAAACACCTGTGGTTCTTCCTCCTCCTGGTGGCAGCTCCCAGATGGGTCCTGTCCCAGGTGCAGCTGCAGGAGTCGGGCCCAGGACTGGTGAAGCCTTCGGAGACCCTGTCCCTCACCTGCACTGTCTCTGGTGGCTCCATCAGTAGTTACTACTGGAGCTGGATCCGGCAGCCCGCCGGGAAGGGACTGGAGTGGATTGGGCGTATCTATACCAGTGGGAGCACCAACTACAACCCCTCCCTCAAGAGTCGAGTCACCATGTCAGTAGACACGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCCGCGGACACGGCCGTGTATTACTGTGCGAGAGTAGGCTATAGAGCAGCAGCTGGTACTGATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
        'AAACGGGAGCGACGTA-1_contig_2':
        'TCTGGCACCAGGGGTCCCTTCCAATATCAGCACCATGGCCTGGACTCCTCTCTTTCTGTTCCTCCTCACTTGCTGCCCAGGGTCCAATTCCCAGGCTGTGGTGACTCAGGAGCCCTCACTGACTGTGTCCCCAGGAGGGACAGTCACTCTCACCTGTGGCTCCAGCACTGGAGCTGTCACCAGTGGTCATTATCCCTACTGGTTCCAGCAGAAGCCTGGCCAAGCCCCCAGGACACTGATTTATGATACAAGCAACAAACACTCCTGGACACCTGCCCGGTTCTCAGGCTCCCTCCTTGGGGGCAAAGCTGCCCTGACCCTTTCGGGTGCGCAGCCTGAGGATGAGGCTGAGTATTACTGCTTGCTCTCCTATAGTGGTGCTAGGGGTGTTCGGCGGAGGGACCAAGCTGACCGTCCTAGGTCAGCCCAAGGCTGCCCCCTCGGTCACTCTGTTCCCGCCCTCCTCTGAGGAGCTTCAAGCCAACAAGGCCACACTGGTGTGTCTCATAAGTGACTTCTACCCGGGAGCCGTGACAGTGGCCTGGAAGGCAGATAGCAGCCCCGTCAAGGCGGGAGTGGAGACCACCACACCCTCCAAACAAAGCAACAACAAGTACGCGGCCAGCAGCTA'
    }
    return (seq)


@pytest.fixture
def annotation_10x():
    """Standard cellranger annotation file to test the preprocessing."""
    annot = pd.DataFrame([
        [
            'AAACCTGTCATATCGG-1', 'True', 'AAACCTGTCATATCGG-1_contig_1',
            'True', '556', 'IGK', 'IGKV1-8', 'None', 'IGKJ4', 'IGKC', 'True',
            'True', 'CQQYDELPVTF', 'TGTCAACAATATGACGAACTTCCCGTCACTTTC', '9139',
            '68', 'clonotype9', 'clonotype9_consensus_1'
        ],
        [
            'AAACCTGTCCGTTGTC-1', 'True', 'AAACCTGTCCGTTGTC-1_contig_1',
            'True', '551', 'IGK', 'IGKV1-8', 'None', 'IGKJ1', 'IGKC', 'True',
            'True', 'CQQYYSYPRTF', 'TGTCAACAGTATTATAGTTACCCTCGGACGTTC', '5679',
            '43', 'clonotype10', 'clonotype10_consensus_1'
        ],
        [
            'AAACCTGTCCGTTGTC-1', 'True', 'AAACCTGTCCGTTGTC-1_contig_2',
            'True', '565', 'IGH', 'IGHV1-69D', 'IGHD3-22', 'IGHJ3', 'IGHM',
            'True', 'True', 'CATTYYYDSSGYYQNDAFDIW',
            'TGTGCGACTACGTATTACTATGATAGTAGTGGTTATTACCAGAATGATGCTTTTGATATCTGG',
            '4161', '51', 'clonotype10', 'clonotype10_consensus_2'
        ],
        [
            'AAACCTGTCGAGAACG-1', 'True', 'AAACCTGTCGAGAACG-1_contig_1',
            'True', '642', 'IGL', 'IGLV5-45', 'None', 'IGLJ3', 'IGLC3', 'True',
            'True', 'CMIWHSSAWVV', 'TGTATGATTTGGCACAGCAGCGCTTGGGTGGTC',
            '13160', '90', 'clonotype11', 'clonotype11_consensus_1'
        ],
        [
            'AAACCTGTCGAGAACG-1', 'True', 'AAACCTGTCGAGAACG-1_contig_2',
            'True', '550', 'IGH', 'IGHV1-2', 'None', 'IGHJ3', 'IGHM', 'True',
            'True', 'CAREIEGDGVFEIW',
            'TGTGCGAGAGAGATAGAGGGGGACGGTGTTTTTGAAATCTGG', '5080', '47',
            'clonotype11', 'clonotype11_consensus_2'
        ],
        [
            'AAACCTGTCTTGAGAC-1', 'True', 'AAACCTGTCTTGAGAC-1_contig_1',
            'True', '551', 'IGK', 'IGKV1D-8', 'None', 'IGKJ2', 'IGKC', 'True',
            'True', 'CQQYYSFPYTF', 'TGTCAACAGTATTATAGTTTCCCGTACACTTTT', '2813',
            '22', 'clonotype12', 'clonotype12_consensus_1'
        ],
        [
            'AAACCTGTCTTGAGAC-1', 'True', 'AAACCTGTCTTGAGAC-1_contig_2',
            'True', '557', 'IGH', 'IGHV5-51', 'None', 'IGHJ3', 'IGHM', 'True',
            'True', 'CARHIRGNRFGNDAFDIW',
            'TGTGCGAGACATATCCGTGGGAACAGATTTGGCAATGATGCTTTTGATATCTGG', '8292',
            '80', 'clonotype12', 'clonotype12_consensus_2'
        ],
        [
            'AAACGGGAGCGACGTA-1', 'True', 'AAACGGGAGCGACGTA-1_contig_1',
            'True', '534', 'IGH', 'IGHV4-59', 'None', 'IGHJ3', 'IGHM', 'True',
            'True', 'CARVGYRAAAGTDAFDIW',
            'TGTGCGAGAGTAGGCTATAGAGCAGCAGCTGGTACTGATGCTTTTGATATCTGG', '1235',
            '18', 'clonotype13', 'clonotype13_consensus_1'
        ],
        [
            'AAACGGGAGCGACGTA-1', 'True', 'AAACGGGAGCGACGTA-1_contig_2',
            'True', '631', 'IGL', 'IGLV7-46', 'None', 'IGLJ3', 'IGLC2', 'True',
            'False', 'None', 'None', '739', '8', 'clonotype13', 'None'
        ],
    ],
        columns=[
        'barcode', 'is_cell', 'contig_id',
        'high_confidence', 'length', 'chain', 'v_gene',
        'd_gene', 'j_gene', 'c_gene', 'full_length',
        'productive', 'cdr3', 'cdr3_nt', 'reads', 'umis',
        'raw_clonotype_id', 'raw_consensus_id'
    ])

    return (annot)


@pytest.fixture
def airr_10x():
    """Standard cellranger airr file to test the preprocessing."""
    airr = pd.DataFrame([
        [
            'AAACCTGTCATATCGG-1', '', 'AAACCTGTCATATCGG-1_contig_1',
            'TGGGGAGGAGTCAGTCCCAACCAGGACACGGCCTGGACATGAGGGTCCCTGCTCAGCTCCTGGGGCTCCTGCTGCTCTGGCTCTCAGGTGCCAGATGTGACATCCAGATGACCCAGTCTCCATCCTCCCTGTCTGCATCTGTGGGAGACAGAGTCACCATCACTTGCCAGGCGACACAAGACATTAACAATTATGTAAATTGGTATCAGCAGAAACCAGGGAAAGCCCCTAAACTCCTGATCTACGATGCATTGAATTTAGAAATAGGGGTCCCATCAAGATTCAGTGGAAGAGGGTCTGGGACAGTCTTTATTCTCACCATCAGCAGCCTGCAGCCTGAAGATGTTGCAACATACTACTGTCAACAATATGACGAACTTCCCGTCACTTTCGGCGGAGGGACCAATGTGGAAATGAGACGAACTGTGGCTGCACCATCTGTCTTCATCTTCCCGCCATCTGATGAGCAGTTGAAATCTGGAACTGCCTCTGTTGTGTGCCTGCTGAATAACTTCTATCCCAGAGAGGCCAAAGTACAGTGGAAGGTGGATAACGC',
            'MRVPAQLLGLLLLWLSGARCDIQMTQSPSSLSASVGDRVTITCQATQDINNYVNWYQQKPGKAPKLLIYDALNLEIGVPSRFSGRGSGTVFILTISSLQPEDVATYYCQQYDELPVTFGGGTNVEMRRTVAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDN',
            'T', 'F', 'IGKV1-8', '38S314M204S', '', '', 'IGKJ4', '383S37M136S',
            'IGKC', '420S136M',
            'TGGGGAGGAGTCAGTCCCAACCAGGACACGGCCTGGACATGAGGGTCCCTGCTCAGCTCCTGGGGCTCCTGCTGCTCTGGCTCTCAGGTGCCAGATGTGACATCCAGATGACCCAGTCTCCATCCTCCCTGTCTGCATCTGTGGGAGACAGAGTCACCATCACTTGCCAGGCGACACAAGACATTAACAATTATGTAAATTGGTATCAGCAGAAACCAGGGAAAGCCCCTAAACTCCTGATCTACGATGCATTGAATTTAGAAATAGGGGTCCCATCAAGATTCAGTGGAAGAGGGTCTGGGACAGTCTTTATTCTCACCATCAGCAGCCTGCAGCCTGAAGATGTTGCAACATACTACTGTCAACAATATGACGAACTTCCCGTCACTTTCGGCGGAGGGACCAATGTGGAAATGAGACGAACTGTGGCTGCACCATCTGTCTTCATCTTCCCGCCATCTGATGAGCAGTTGAAATCTGGAACTGCCTCTGTTGTGTGCCTGCTGAATAACTTCTATCCCAGAGAGGCCAAAGTACAGTGGAAGGTGGATAACGC',
            'ATGAGGGTCCCCGCTCAGCTCCTGGGGCTCCTGCTGCTCTGGCTCCCAGGTGCCAGATGTGCCATCCGGATGACCCAGTCTCCATCCTCATTCTCTGCATCTACAGGAGACAGAGTCACCATCACTTGTCGGGCGAGTCAGGGTATTAGCAGTTATTTAGCCTGGTATCAGCAAAAACCAGGGAAAGCCCCTAAGCTCCTGATCTATGCTGCATCCACTTTGCAAAGTGGGGTCCCATCAAGGTTCAGCGGCAGTGGATCTGGGACAGATTTCACTCTCACCATCAGCTGCCTGCAGTCTGAAGATTTTGCAACTTATTACTGTCAACAGTATTATAGTTACCCTCTCACTTTCGGCGGAGGGACCAAGGTGGAGATCAAACGAACTGTGGCTGCACCATCTGTCTTCATCTTCCCGCCATCTGATGAGCAGTTGAAATCTGGAACTGCCTCTGTTGTGTGCCTGCTGAATAACTTCTATCCCAGAGAGGCCAAAGTACAGTGGAAGGTGGATAACGC',
            'TGTCAACAATATGACGAACTTCCCGTCACTTTC', 'CQQYDELPVTF', '33', '11',
            '39', '352', '', '', '384', '420', '421', '556', '9139', '68', 'T'
        ],
        [
            'AAACCTGTCCGTTGTC-1', '', 'AAACCTGTCCGTTGTC-1_contig_1',
            'AGGAGTCAGACCCTGTCAGGACACAGCATAGACATGAGGGTCCCCGCTCAGCTCCTGGGGCTCCTGCTGCTCTGGCTCCCAGGTGCCAGATGTGCCATCCGGATGACCCAGTCTCCATCCTCATTCTCTGCATCTACAGGAGACAGAGTCACCATCACTTGTCGGGCGAGTCAGGGTATTAGCAGTTATTTAGCCTGGTATCAGCAAAAACCAGGGAAAGCCCCTAAGCTCCTGATCTATGCTGCATCCACTTTGCAAAGTGGGGTCCCATCAAGGTTCAGCGGCAGTGGATCTGGGACAGATTTCACTCTCACCATCAGCTGCCTGCAGTCTGAAGATTTTGCAACTTATTACTGTCAACAGTATTATAGTTACCCTCGGACGTTCGGCCAAGGGACCAAGGTGGAAATCAAACGAACTGTGGCTGCACCATCTGTCTTCATCTTCCCGCCATCTGATGAGCAGTTGAAATCTGGAACTGCCTCTGTTGTGTGCCTGCTGAATAACTTCTATCCCAGAGAGGCCAAAGTACAGTGGAAGGTGGATAACGC',
            'MRVPAQLLGLLLLWLPGARCAIRMTQSPSSFSASTGDRVTITCRASQGISSYLAWYQQKPGKAPKLLIYAASTLQSGVPSRFSGSGSGTDFTLTISCLQSEDFATYYCQQYYSYPRTFGQGTKVEIKRTVAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDN',
            'T', 'F', 'IGKV1-8', '33S345M173S', '', '', 'IGKJ1', '377S38M136S',
            'IGKC', '415S136M',
            'AGGAGTCAGACCCTGTCAGGACACAGCATAGACATGAGGGTCCCCGCTCAGCTCCTGGGGCTCCTGCTGCTCTGGCTCCCAGGTGCCAGATGTGCCATCCGGATGACCCAGTCTCCATCCTCATTCTCTGCATCTACAGGAGACAGAGTCACCATCACTTGTCGGGCGAGTCAGGGTATTAGCAGTTATTTAGCCTGGTATCAGCAAAAACCAGGGAAAGCCCCTAAGCTCCTGATCTATGCTGCATCCACTTTGCAAAGTGGGGTCCCATCAAGGTTCAGCGGCAGTGGATCTGGGACAGATTTCACTCTCACCATCAGCTGCCTGCAGTCTGAAGATTTTGCAACTTATTACTGTCAACAGTATTATAGTTACCCTCGGACGTTCGGCCAAGGGACCAAGGTGGAAATCAAACGAACTGTGGCTGCACCATCTGTCTTCATCTTCCCGCCATCTGATGAGCAGTTGAAATCTGGAACTGCCTCTGTTGTGTGCCTGCTGAATAACTTCTATCCCAGAGAGGCCAAAGTACAGTGGAAGGTGGATAACGC',
            'AGGCTGGACACACTTCATGCAGGAGTCAGACCCTGTCAGGACACAGCATAGACATGAGGGTCCCCGCTCAGCTCCTGGGGCTCCTGCTGCTCTGGCTCCCAGGTGCCAGATGTGCCATCCGGATGACCCAGTCTCCATCCTCATTCTCTGCATCTACAGGAGACAGAGTCACCATCACTTGTCGGGCGAGTCAGGGTATTAGCAGTTATTTAGCCTGGTATCAGCAAAAACCAGGGAAAGCCCCTAAGCTCCTGATCTATGCTGCATCCACTTTGCAAAGTGGGGTCCCATCAAGGTTCAGCGGCAGTGGATCTGGGACAGATTTCACTCTCACCATCAGCTGCCTGCAGTCTGAAGATTTTGCAACTTATTACTGTCAACAGTATTATAGTTACCCTGTGGACGTTCGGCCAAGGGACCAAGGTGGAAATCAAACGAACTGTGGCTGCACCATCTGTCTTCATCTTCCCGCCATCTGATGAGCAGTTGAAATCTGGAACTGCCTCTGTTGTGTGCCTGCTGAATAACTTCTATCCCAGAGAGGCCAAAGTACAGTGGAAGGTGGATAACGC',
            'TGTCAACAGTATTATAGTTACCCTCGGACGTTC', 'CQQYYSYPRTF', '33', '11',
            '34', '378', '', '', '378', '415', '416', '551', '5679', '43', 'T'
        ],
        [
            'AAACCTGTCCGTTGTC-1', '', 'AAACCTGTCCGTTGTC-1_contig_2',
            'ATCACATAACAACCACATTCCTCCTCTAAAGAAGCCCCTGGGAGCACAGCTCATCACCATGGACTGGACCTGGAGGTTCCTCTTTGTGGTGGCAGCAGCTACAGGTGTCCAGTCCCAGGTGCAGCTGGTGCAGTCTGGGGCTGAGGTGAAGAAGCCTGGGTCCTCGGTGAAGGTCTCCTGCAAGGCTTCTGGAGGCACCTTCAGCAGCTATGCTATCAGCTGGGTGCGACAGGCCCCTGGACAAGGGCTTGAGTGGATGGGAGGGATCATCCCTATCTTTGGTACAGCAAACTACGCACAGAAGTTCCAGGGCAGAGTCACGATTACCGCGGACGAATCCACGAGCACAGCCTACATGGAGCTGAGCAGCCTGAGATCTGAGGACACGGCCGTGTATTACTGTGCGACTACGTATTACTATGATAGTAGTGGTTATTACCAGAATGATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
            'MDWTWRFLFVVAAATGVQSQVQLVQSGAEVKKPGSSVKVSCKASGGTFSSYAISWVRQAPGQGLEWMGGIIPIFGTANYAQKFQGRVTITADESTSTAYMELSSLRSEDTAVYYCATTYYYDSSGYYQNDAFDIWGQGTMVTVSSGSASAPTLFPLVSCENSPSDTSSV',
            'T', 'F', 'IGHV1-69D', '58S353M154S', 'IGHD3-22', '411S31M123S',
            'IGHJ3', '444S50M71S', 'IGHM', '494S71M',
            'ATCACATAACAACCACATTCCTCCTCTAAAGAAGCCCCTGGGAGCACAGCTCATCACCATGGACTGGACCTGGAGGTTCCTCTTTGTGGTGGCAGCAGCTACAGGTGTCCAGTCCCAGGTGCAGCTGGTGCAGTCTGGGGCTGAGGTGAAGAAGCCTGGGTCCTCGGTGAAGGTCTCCTGCAAGGCTTCTGGAGGCACCTTCAGCAGCTATGCTATCAGCTGGGTGCGACAGGCCCCTGGACAAGGGCTTGAGTGGATGGGAGGGATCATCCCTATCTTTGGTACAGCAAACTACGCACAGAAGTTCCAGGGCAGAGTCACGATTACCGCGGACGAATCCACGAGCACAGCCTACATGGAGCTGAGCAGCCTGAGATCTGAGGACACGGCCGTGTATTACTGTGCGACTACGTATTACTATGATAGTAGTGGTTATTACCAGAATGATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
            'ATCACATAACAACCACATTCCTCCTCTAAAGAAGCCCCTGGGAGCACAGCTCATCACCATGGACTGGACCTGGAGGTTCCTCTTTGTGGTGGCAGCAGCTACAGGTGTCCAGTCCCAGGTGCAGCTGGTGCAGTCTGGGGCTGAGGTGAAGAAGCCTGGGTCCTCGGTGAAGGTCTCCTGCAAGGCTTCTGGAGGCACCTTCAGCAGCTATGCTATCAGCTGGGTGCGACAGGCCCCTGGACAAGGGCTTGAGTGGATGGGAGGGATCATCCCTATCTTTGGTACAGCAAACTACGCACAGAAGTTCCAGGGCAGAGTCACGATTACCGCGGACGAATCCACGAGCACAGCCTACATGGAGCTGAGCAGCCTGAGATCTGAGGACACGGCCGTGTATTACTGTGCGAGAGAGTATTACTATGATAGTAGTGGTTATTACTACTGATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
            'TGTGCGACTACGTATTACTATGATAGTAGTGGTTATTACCAGAATGATGCTTTTGATATCTGG',
            'CATTYYYDSSGYYQNDAFDIW', '63', '21', '59', '411', '412', '442',
            '445', '494', '495', '565', '4161', '51', 'T'
        ],
        [
            'AAACCTGTCGAGAACG-1', '', 'AAACCTGTCGAGAACG-1_contig_1',
            'ACTGTGGGGGTAAGAGGTTGTGTCCACCATGGCCTGGACTCCTCTCCTCCTCCTGTTCCTCTCTCACTGCACAGGTTCCCTCTCGCAGGCTGTGCTGACTCAGCCGTCTTCCCTCTCTGCATCTCCTGGAGCATCAGGCAGGCTCACCTGCACCTTACGCAGTGACATCAATGTTGGTACGTACAGGATATATTGGTACCAGCGGAAGCCAGGGAGTCCTCCCCAGTATCTCCTGAGGTACAAATCAGACTCAGATAAGCAGCAGGGCTCTGGAGTCCCCAGCCGCTTCTCTGGATCCAAAGATGCTTCGGCCAATGCAGGGATTTTACTCATCTCTGGGCTCCAGTCTGAGGATGAGGCTGACTATTATTGTATGATTTGGCACAGCAGCGCTTGGGTGGTCGGCGGAGGGACCAAGCTGACCGTCCTAGGTCAGCCCAAGGCTGCCCCCTCGGTCACTCTGTTCCCACCCTCCTCTGAGGAGCTTCAAGCCAACAAGGCCACACTGGTGTGTCTCATAAGTGACTTCTACCCGGGAGCCGTGACAGTGGCCTGGAAGGCAGATAGCAGCCCCGTCAAGGCGGGAGTGGAGACCACCACACCCTCCAAACAAAGCAACAACAAGTACGCGGCCAGCAGCTA',
            'MAWTPLLLLFLSHCTGSLSQAVLTQPSSLSASPGASGRLTCTLRSDINVGTYRIYWYQRKPGSPPQYLLRYKSDSDKQQGSGVPSRFSGSKDASANAGILLISGLQSEDEADYYCMIWHSSAWVVGGGTKLTVLGQPKAAPSVTLFPPSSEELQANKATLVCLISDFYPGAVTVAWKADSSPVKAGVETTTPSKQSNNKYAASS',
            'T', 'F', 'IGLV5-45', '28S369M245S', '', '', 'IGLJ3',
            '393S38M211S', 'IGLC3', '431S211M',
            'ACTGTGGGGGTAAGAGGTTGTGTCCACCATGGCCTGGACTCCTCTCCTCCTCCTGTTCCTCTCTCACTGCACAGGTTCCCTCTCGCAGGCTGTGCTGACTCAGCCGTCTTCCCTCTCTGCATCTCCTGGAGCATCAGGCAGGCTCACCTGCACCTTACGCAGTGACATCAATGTTGGTACGTACAGGATATATTGGTACCAGCGGAAGCCAGGGAGTCCTCCCCAGTATCTCCTGAGGTACAAATCAGACTCAGATAAGCAGCAGGGCTCTGGAGTCCCCAGCCGCTTCTCTGGATCCAAAGATGCTTCGGCCAATGCAGGGATTTTACTCATCTCTGGGCTCCAGTCTGAGGATGAGGCTGACTATTATTGTATGATTTGGCACAGCAGCGCTTGGGTGGTCGGCGGAGGGACCAAGCTGACCGTCCTAGGTCAGCCCAAGGCTGCCCCCTCGGTCACTCTGTTCCCACCCTCCTCTGAGGAGCTTCAAGCCAACAAGGCCACACTGGTGTGTCTCATAAGTGACTTCTACCCGGGAGCCGTGACAGTGGCCTGGAAGGCAGATAGCAGCCCCGTCAAGGCGGGAGTGGAGACCACCACACCCTCCAAACAAAGCAACAACAAGTACGCGGCCAGCAGCTA',
            'ACTGCGGGGGTAAGAGGTTGTGTCCACCATGGCCTGGACTCCTCTCCTCCTCCTGTTCCTCTCTCACTGCACAGGTTCCCTCTCGCAGGCTGTGCTGACTCAGCCGTCTTCCCTCTCTGCATCTCCTGGAGCATCAGCCAGTCTCACCTGCACCTTGCGCAGTGGCATCAATGTTGGTACCTACAGGATATACTGGTACCAGCAGAAGCCAGGGAGTCCTCCCCAGTATCTCCTGAGGTACAAATCAGACTCAGATAAGCAGCAGGGCTCTGGAGTCCCCAGCCGCTTCTCTGGATCCAAAGATGCTTCGGCCAATGCAGGGATTTTACTCATCTCTGGGCTCCAGTCTGAGGATGAGGCTGACTATTACTGTATGATTTGGCACAGCAGCGCTTCTTTGGGTGTTCGGCGGAGGGACCAAGCTGACCGTCCTAGGTCAGCCCAAGGCTGCCCCCTCGGTCACTCTGTTCCCACCCTCCTCTGAGGAGCTTCAAGCCAACAAGGCCACACTGGTGTGTCTCATAAGTGACTTCTACCCGGGAGCCGTGACAGTGGCCTGGAAGGCAGATAGCAGCCCCGTCAAGGCGGGAGTGGAGACCACCACACCCTCCAAACAAAGCAACAACAAGTACGCGGCCAGCAGCTA',
            'TGTATGATTTGGCACAGCAGCGCTTGGGTGGTC', 'CMIWHSSAWVV', '33', '11',
            '29', '397', '', '', '394', '431', '432', '642', '13160', '90', 'T'
        ],
        [
            'AAACCTGTCGAGAACG-1', '', 'AAACCTGTCGAGAACG-1_contig_2',
            'GGGAGCATCACCCAGCAACCACATCTGTCCTCTAGAGAATCCCCTGAGAGCTCCGTTCCTCACCATGGACTGGACCTGGAGGATCCTCTTCTTGGTGGCAGCAGCCACAGGAGCCCACTCGCAGGTGCAACTGGTGCAGTCTGGGGGTGAGGTAAAGAAGCCTGGGGCCTCAGTGAAGGTCTCCTGCAAGGCTTCTGGATACACCTTCACCGACTACTTCATACAGTGGCTGCGACACGCCCCTGGACAGGGGCTTGATTGGATGGGTTTAATCAACCCTAACAGTGGTGACACCAACTATGCACAGAAGTTTCAGGGCAGAGTCACCATGACCAGGGACACGTCCATCAGTACAGCCTACATGGAACTGAGCAGCCTGAGATCTGACGACACGGCCGTATATTACTGTGCGAGAGAGATAGAGGGGGACGGTGTTTTTGAAATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
            'MDWTWRILFLVAAATGAHSQVQLVQSGGEVKKPGASVKVSCKASGYTFTDYFIQWLRHAPGQGLDWMGLINPNSGDTNYAQKFQGRVTMTRDTSISTAYMELSSLRSDDTAVYYCAREIEGDGVFEIWGQGTMVTVSSGSASAPTLFPLVSCENSPSDTSSV',
            'T', 'F', 'IGHV1-2', '64S353M133S', '', '', 'IGHJ3', '429S50M71S',
            'IGHM', '479S71M',
            'GGGAGCATCACCCAGCAACCACATCTGTCCTCTAGAGAATCCCCTGAGAGCTCCGTTCCTCACCATGGACTGGACCTGGAGGATCCTCTTCTTGGTGGCAGCAGCCACAGGAGCCCACTCGCAGGTGCAACTGGTGCAGTCTGGGGGTGAGGTAAAGAAGCCTGGGGCCTCAGTGAAGGTCTCCTGCAAGGCTTCTGGATACACCTTCACCGACTACTTCATACAGTGGCTGCGACACGCCCCTGGACAGGGGCTTGATTGGATGGGTTTAATCAACCCTAACAGTGGTGACACCAACTATGCACAGAAGTTTCAGGGCAGAGTCACCATGACCAGGGACACGTCCATCAGTACAGCCTACATGGAACTGAGCAGCCTGAGATCTGACGACACGGCCGTATATTACTGTGCGAGAGAGATAGAGGGGGACGGTGTTTTTGAAATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
            'GAGAGCATCACCCAGCAACCACATCTGTCCTCTAGAGAATCCCCTGAGAGCTCCGTTCCTCACCATGGACTGGACCTGGAGGATCCTCTTCTTGGTGGCAGCAGCCACAGGAGCCCACTCCCAGGTGCAGCTGGTGCAGTCTGGGGCTGAGGTGAAGAAGCCTGGGGCCTCAGTGAAGGTCTCCTGCAAGGCTTCTGGATACACCTTCACCGGCTACTATATGCACTGGGTGCGACAGGCCCCTGGACAAGGGCTTGAGTGGATGGGATGGATCAACCCTAACAGTGGTGGCACAAACTATGCACAGAAGTTTCAGGGCTGGGTCACCATGACCAGGGACACGTCCATCAGCACAGCCTACATGGAGCTGAGCAGGCTGAGATCTGACGACACGGCCGTGTATTACTGTGCGAGAGATGATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
            'TGTGCGAGAGAGATAGAGGGGGACGGTGTTTTTGAAATCTGG', 'CAREIEGDGVFEIW',
            '42', '14', '65', '417', '', '', '430', '479', '480', '550',
            '5080', '47', 'T'
        ],
        [
            'AAACCTGTCTTGAGAC-1', '', 'AAACCTGTCTTGAGAC-1_contig_1',
            'AGGAGTCAGACCCAGTCAGGACACAGCATGGACATGAGGGTCCCCGCTCAGCTCCTGGGGCTCCTGCTGCTCTGGCTCCCAGGTGCCAGATGTGTCATCTGGATGACCCAGTCTCCATCCTTACTCTCTGCATCTACAGGAGACAGAGTCACCATCAGTTGTCGGATGAGTCAGGGCATTAGCAGTTATTTAGCCTGGTATCAGCAAAAACCAGGGAAAGCCCCTGAGCTCCTGATCTATGCTGCATCCACTTTGCAAAGTGGGGTCCCATCAAGGTTCAGTGGCAGTGGATCTGGGACAGATTTCACTCTCACCATCAGTTGCCTGCAGTCTGAAGATTTTGCAACTTATTACTGTCAACAGTATTATAGTTTCCCGTACACTTTTGGCCAGGGGACCAAGCTGGAGATCAAACGAACTGTGGCTGCACCATCTGTCTTCATCTTCCCGCCATCTGATGAGCAGTTGAAATCTGGAACTGCCTCTGTTGTGTGCCTGCTGAATAACTTCTATCCCAGAGAGGCCAAAGTACAGTGGAAGGTGGATAACGC',
            'MDMRVPAQLLGLLLLWLPGARCVIWMTQSPSLLSASTGDRVTISCRMSQGISSYLAWYQQKPGKAPELLIYAASTLQSGVPSRFSGSGSGTDFTLTISCLQSEDFATYYCQQYYSFPYTFGQGTKLEIKRTVAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDN',
            'T', 'F', 'IGKV1D-8', '27S353M171S', '', '', 'IGKJ2',
            '376S39M136S', 'IGKC', '415S136M',
            'AGGAGTCAGACCCAGTCAGGACACAGCATGGACATGAGGGTCCCCGCTCAGCTCCTGGGGCTCCTGCTGCTCTGGCTCCCAGGTGCCAGATGTGTCATCTGGATGACCCAGTCTCCATCCTTACTCTCTGCATCTACAGGAGACAGAGTCACCATCAGTTGTCGGATGAGTCAGGGCATTAGCAGTTATTTAGCCTGGTATCAGCAAAAACCAGGGAAAGCCCCTGAGCTCCTGATCTATGCTGCATCCACTTTGCAAAGTGGGGTCCCATCAAGGTTCAGTGGCAGTGGATCTGGGACAGATTTCACTCTCACCATCAGTTGCCTGCAGTCTGAAGATTTTGCAACTTATTACTGTCAACAGTATTATAGTTTCCCGTACACTTTTGGCCAGGGGACCAAGCTGGAGATCAAACGAACTGTGGCTGCACCATCTGTCTTCATCTTCCCGCCATCTGATGAGCAGTTGAAATCTGGAACTGCCTCTGTTGTGTGCCTGCTGAATAACTTCTATCCCAGAGAGGCCAAAGTACAGTGGAAGGTGGATAACGC',
            'GGGACACCTGGGGACACTGAGCTGGTGCTGAGTTACTGAGATGAGCCAGCTCTGCAGCTGTGCCCAGTCAGCCCCATCCCCTGCTCATTTGCATGTTCCCAGAGCACAACCTCCTGCACTGAAGCCTTATTAATAGGCTGGCCACACTTCATGCAGGAGTCAGACCCAGTCAGGACACAGCATGGACATGAGGGTCCCCGCTCAGCTCCTGGGGCTCCTGCTGCTCTGGCTCCCAGGTGCCAGATGTGTCATCTGGATGACCCAGTCTCCATCCTTACTCTCTGCATCTACAGGAGACAGAGTCACCATCAGTTGTCGGATGAGTCAGGGCATTAGCAGTTATTTAGCCTGGTATCAGCAAAAACCAGGGAAAGCCCCTGAGCTCCTGATCTATGCTGCATCCACTTTGCAAAGTGGGGTCCCATCAAGGTTCAGTGGCAGTGGATCTGGGACAGATTTCACTCTCACCATCAGTTGCCTGCAGTCTGAAGATTTTGCAACTTATTACTGTCAACAGTATTATAGTTTCCCTCCTGTGCAGTTTTGGCCAGGGGACCAAGCTGGAGATCAAACGAACTGTGGCTGCACCATCTGTCTTCATCTTCCCGCCATCTGATGAGCAGTTGAAATCTGGAACTGCCTCTGTTGTGTGCCTGCTGAATAACTTCTATCCCAGAGAGGCCAAAGTACAGTGGAAGGTGGATAACGC',
            'TGTCAACAGTATTATAGTTTCCCGTACACTTTT', 'CQQYYSFPYTF', '33', '11',
            '28', '380', '', '', '377', '415', '416', '551', '2813', '22', 'T'
        ],
        [
            'AAACCTGTCTTGAGAC-1', '', 'AAACCTGTCTTGAGAC-1_contig_2',
            'GGAGTCTCCCTCACCGCCCAGCTGGGATCTCAGGGCTTCATTTTCTGTCCTCCACCATCATGGGGTCAACCGCCATCCTCGCCCTCCTCCTGGCTGTTCTCCAAGGAGTCTGTGCCGAGGTGCAGCTGGTGCAGTCTGGAGCAGAGGTGAAAAAGCCGGGGGAGTCTCTGAAGATCTCCTGTAAGGGTTCTGGATACAGCTTTACCAGCTACTGGATCGGCTGGGTGCGCCAGATGCCCGGGAAAGGCCTGGAGTGGATGGGGATCATCTATCCTGGTGACTCTGATACCAGATACAGCCCGTCCTTCCAAGGCCAGGTCACCATCTCAGCCGACAAGTCCATCAGCACCGCCTACCTGCAGTGGAGCAGCCTGAAGGCCTCGGACACCGCCATGTATTACTGTGCGAGACATATCCGTGGGAACAGATTTGGCAATGATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
            'MGSTAILALLLAVLQGVCAEVQLVQSGAEVKKPGESLKISCKGSGYSFTSYWIGWVRQMPGKGLEWMGIIYPGDSDTRYSPSFQGQVTISADKSISTAYLQWSSLKASDTAMYYCARHIRGNRFGNDAFDIWGQGTMVTVSSGSASAPTLFPLVSCENSPSDTSSV',
            'T', 'F', 'IGHV5-51', '59S353M145S', '', '', 'IGHJ3', '436S50M71S',
            'IGHM', '486S71M',
            'GGAGTCTCCCTCACCGCCCAGCTGGGATCTCAGGGCTTCATTTTCTGTCCTCCACCATCATGGGGTCAACCGCCATCCTCGCCCTCCTCCTGGCTGTTCTCCAAGGAGTCTGTGCCGAGGTGCAGCTGGTGCAGTCTGGAGCAGAGGTGAAAAAGCCGGGGGAGTCTCTGAAGATCTCCTGTAAGGGTTCTGGATACAGCTTTACCAGCTACTGGATCGGCTGGGTGCGCCAGATGCCCGGGAAAGGCCTGGAGTGGATGGGGATCATCTATCCTGGTGACTCTGATACCAGATACAGCCCGTCCTTCCAAGGCCAGGTCACCATCTCAGCCGACAAGTCCATCAGCACCGCCTACCTGCAGTGGAGCAGCCTGAAGGCCTCGGACACCGCCATGTATTACTGTGCGAGACATATCCGTGGGAACAGATTTGGCAATGATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
            'TGAGTCTCCCTCACTGCCCAGCTGGGATCTCAGGGCTTCATTTTCTGTCCTCCACCATCATGGGGTCAACCGCCATCCTCGCCCTCCTCCTGGCTGTTCTCCAAGGAGTCTGTGCCGAGGTGCAGCTGGTGCAGTCTGGAGCAGAGGTGAAAAAGCCCGGGGAGTCTCTGAAGATCTCCTGTAAGGGTTCTGGATACAGCTTTACCAGCTACTGGATCGGCTGGGTGCGCCAGATGCCCGGGAAAGGCCTGGAGTGGATGGGGATCATCTATCCTGGTGACTCTGATACCAGATACAGCCCGTCCTTCCAAGGCCAGGTCACCATCTCAGCCGACAAGTCCATCAGCACCGCCTACCTGCAGTGGAGCAGCCTGAAGGCCTCGGACACCGCCATGTATTACTGTGCGAGACATGATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
            'TGTGCGAGACATATCCGTGGGAACAGATTTGGCAATGATGCTTTTGATATCTGG',
            'CARHIRGNRFGNDAFDIW', '54', '18', '60', '412', '', '', '437',
            '486', '487', '557', '8292', '80', 'T'
        ],
        [
            'AAACGGGAGCGACGTA-1', '', 'AAACGGGAGCGACGTA-1_contig_1',
            'GGGGACTTTCTGAGACTCATGGACCTCCTGCACAAGAACATGAAACACCTGTGGTTCTTCCTCCTCCTGGTGGCAGCTCCCAGATGGGTCCTGTCCCAGGTGCAGCTGCAGGAGTCGGGCCCAGGACTGGTGAAGCCTTCGGAGACCCTGTCCCTCACCTGCACTGTCTCTGGTGGCTCCATCAGTAGTTACTACTGGAGCTGGATCCGGCAGCCCGCCGGGAAGGGACTGGAGTGGATTGGGCGTATCTATACCAGTGGGAGCACCAACTACAACCCCTCCCTCAAGAGTCGAGTCACCATGTCAGTAGACACGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCCGCGGACACGGCCGTGTATTACTGTGCGAGAGTAGGCTATAGAGCAGCAGCTGGTACTGATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
            'MKHLWFFLLLVAAPRWVLSQVQLQESGPGLVKPSETLSLTCTVSGGSISSYYWSWIRQPAGKGLEWIGRIYTSGSTNYNPSLKSRVTMSVDTSKNQFSLKLSSVTAADTAVYYCARVGYRAAAGTDAFDIWGQGTMVTVSSGSASAPTLFPLVSCENSPSDTSSV',
            'T', 'F', 'IGHV4-59', '39S350M145S', '', '', 'IGHJ3', '413S50M71S',
            'IGHM', '463S71M',
            'GGGGACTTTCTGAGACTCATGGACCTCCTGCACAAGAACATGAAACACCTGTGGTTCTTCCTCCTCCTGGTGGCAGCTCCCAGATGGGTCCTGTCCCAGGTGCAGCTGCAGGAGTCGGGCCCAGGACTGGTGAAGCCTTCGGAGACCCTGTCCCTCACCTGCACTGTCTCTGGTGGCTCCATCAGTAGTTACTACTGGAGCTGGATCCGGCAGCCCGCCGGGAAGGGACTGGAGTGGATTGGGCGTATCTATACCAGTGGGAGCACCAACTACAACCCCTCCCTCAAGAGTCGAGTCACCATGTCAGTAGACACGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCCGCGGACACGGCCGTGTATTACTGTGCGAGAGTAGGCTATAGAGCAGCAGCTGGTACTGATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
            'ATGAAACATCTGTGGTTCTTCCTTCTCCTGGTGGCAGCTCCCAGATGGGTCCTGTCCCAGGTGCAGCTGCAGGAGTCGGGCCCAGGACTGGTGAAGCCTTCGGAGACCCTGTCCCTCACCTGCACTGTCTCTGGTGGCTCCATCAGTAGTTACTACTGGAGCTGGATCCGGCAGCCCCCAGGGAAGGGACTGGAGTGGATTGGGTATATCTATTACAGTGGGAGCACCAACTACAACCCCTCCCTCAAGAGTCGAGTCACCATATCAGTAGACACGTCCAAGAACCAGTTCTCCCTGAAGCTGAGCTCTGTGACCGCTGCGGACACGGCCGTGTATTACTGTGCGAGAGATGATGCTTTTGATATCTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGGGAGTGCATCCGCCCCAACCCTTTTCCCCCTCGTCTCCTGTGAGAATTCCCCGTCGGATACGAGCAGCGTG',
            'TGTGCGAGAGTAGGCTATAGAGCAGCAGCTGGTACTGATGCTTTTGATATCTGG',
            'CARVGYRAAAGTDAFDIW', '54', '18', '40', '389', '', '', '414',
            '463', '464', '534', '1235', '18', 'T'
        ],
        [
            'AAACGGGAGCGACGTA-1', '', 'AAACGGGAGCGACGTA-1_contig_2',
            'AGCTGTGGGCTCAGAAGCAGAGTTCTGGGGTGTCTCCACCATGGCCTGGACCCCTCTCTGGCTCACTCTCCTCACTCTTTGCATAGGTTCTGTGGTTTCTTCTGAGCTGACTCAGGACCCTGCTGTGTCTGTGGCCTTGGGACAGACAGTCAGGATCACATGCCAAGGAGACAGCCTCAGAAGCTATTATGCAAGCTGGTACCAGCAGAAGCCAGGACAGGCCCCTGTACTTGTCATCTATGGTAAAAACAACCGGCCCTCAGGGATCCCAGACCGATTCTCTGGCTCCAGCTCAGGAAACACAGCTTCCTTGACCATCACTGGGGCTCAGGCGGAAGATGAGGCTGACTATTACTGTAACTCCCGGGACAGCAGTGGTAACCATGTGGTATTCGGCGGAGGGACCAAGCTGACCGTCCTAGGTCAGCCCAAGGCTGCCCCCTCGGTCACTCTGTTCCCGCCCTCCTCTGAGGAGCTTCAAGCCAACAAGGCCACACTGGTGTGTCTCATAAGTGACTTCTACCCGGGAGCCGTGACAGTGGCCTGGAAGGCAGATAGCAGCCCCGTCAAGGCGGGAGTGGAGACCACCACACCCTCCAAACAAAGCAACAACAAGTACGCGGCCAGCAGCTA',
            'MAWTPLWLTLLTLCIGSVVSSELTQDPAVSVALGQTVRITCQGDSLRSYYASWYQQKPGQAPVLVIYGKNNRPSGIPDRFSGSSSGNTASLTITGAQAEDEADYYCNSRDSSGNHVVFGGGTKLTVLGQPKAAPSVTLFPPSSEELQANKATLVCLISDFYPGAVTVAWKADSSPVKAGVETTTPSKQSNNKYAASS',
            'T', 'F', 'IGLV3-19', '40S337M256S', '', '', 'IGLJ2',
            '384S38M211S', 'IGLC2', '422S211M',
            'AGCTGTGGGCTCAGAAGCAGAGTTCTGGGGTGTCTCCACCATGGCCTGGACCCCTCTCTGGCTCACTCTCCTCACTCTTTGCATAGGTTCTGTGGTTTCTTCTGAGCTGACTCAGGACCCTGCTGTGTCTGTGGCCTTGGGACAGACAGTCAGGATCACATGCCAAGGAGACAGCCTCAGAAGCTATTATGCAAGCTGGTACCAGCAGAAGCCAGGACAGGCCCCTGTACTTGTCATCTATGGTAAAAACAACCGGCCCTCAGGGATCCCAGACCGATTCTCTGGCTCCAGCTCAGGAAACACAGCTTCCTTGACCATCACTGGGGCTCAGGCGGAAGATGAGGCTGACTATTACTGTAACTCCCGGGACAGCAGTGGTAACCATGTGGTATTCGGCGGAGGGACCAAGCTGACCGTCCTAGGTCAGCCCAAGGCTGCCCCCTCGGTCACTCTGTTCCCGCCCTCCTCTGAGGAGCTTCAAGCCAACAAGGCCACACTGGTGTGTCTCATAAGTGACTTCTACCCGGGAGCCGTGACAGTGGCCTGGAAGGCAGATAGCAGCCCCGTCAAGGCGGGAGTGGAGACCACCACACCCTCCAAACAAAGCAACAACAAGTACGCGGCCAGCAGCTA',
            'AGCTGTGGGCTCAGAAGCAGAGTTCTGGGGTGTCTCCACCATGGCCTGGACCCCTCTCTGGCTCACTCTCCTCACTCTTTGCATAGGTTCTGTGGTTTCTTCTGAGCTGACTCAGGACCCTGCTGTGTCTGTGGCCTTGGGACAGACAGTCAGGATCACATGCCAAGGAGACAGCCTCAGAAGCTATTATGCAAGCTGGTACCAGCAGAAGCCAGGACAGGCCCCTGTACTTGTCATCTATGGTAAAAACAACCGGCCCTCAGGGATCCCAGACCGATTCTCTGGCTCCAGCTCAGGAAACACAGCTTCCTTGACCATCACTGGGGCTCAGGCGGAAGATGAGGCTGACTATTACTGTAACTCCCGGGACAGCAGTGTGTGGTATTCGGCGGAGGGACCAAGCTGACCGTCCTAGGTCAGCCCAAGGCTGCCCCCTCGGTCACTCTGTTCCCGCCCTCCTCTGAGGAGCTTCAAGCCAACAAGGCCACACTGGTGTGTCTCATAAGTGACTTCTACCCGGGAGCCGTGACAGTGGCCTGGAAGGCAGATAGCAGCCCCGTCAAGGCGGGAGTGGAGACCACCACACCCTCCAAACAAAGCAACAACAAGTACGCGGCCAGCAGCTA',
            'TGTAACTCCCGGGACAGCAGTGGTAACCATGTGGTATTC', 'CNSRDSSGNHVVF', '39',
            '13', '41', '377', '', '', '385', '422', '423', '633', '1344',
            '14', 'T'
        ],
    ],
        columns=[
        'cell_id', 'clone_id', 'sequence_id', 'sequence',
        'sequence_aa', 'productive', 'rev_comp', 'v_call',
        'v_cigar', 'd_call', 'd_cigar', 'j_call',
        'j_cigar', 'c_call', 'c_cigar',
        'sequence_alignment', 'germline_alignment',
        'junction', 'junction_aa', 'junction_length',
        'junction_aa_length', 'v_sequence_start',
        'v_sequence_end', 'd_sequence_start',
        'd_sequence_end', 'j_sequence_start',
        'j_sequence_end', 'c_sequence_start',
        'c_sequence_end', 'consensus_count',
        'duplicate_count', 'is_cell'
    ])
    return (airr)
