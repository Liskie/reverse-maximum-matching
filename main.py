from algorithm import RMMSegmentor

if __name__ == '__main__':
    with open('icwb2-data/testing/msr_test.utf8', 'r') as msr_file:
        text = msr_file.readlines()

    segmentor = RMMSegmentor()
    res = segmentor.segment(text)

    with open('out/msr_out.utf8', 'w') as msr_out:
        for line in res:
            msr_out.write(f'{"  ".join(line)}\n')