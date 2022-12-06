import logging

from inputs import get_file_data
from days.day_6 import part_1, part_2


LOG = logging.getLogger()


class TestDay6Solutions:

    def setup_class(self):
        self.day_6_data = get_file_data('input_day6', False)

    def test_part_1(self):
        assert part_1('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
        assert part_1('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
        assert part_1('nppdvjthqldpwncqszvftbrmjlhg') == 6
        assert part_1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
        assert part_1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

    def test_part_2(self):
        assert part_2('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
        assert part_2('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
        assert part_2('nppdvjthqldpwncqszvftbrmjlhg') == 23
        assert part_2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
        assert part_2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_6_data)}')  # 1034
        LOG.info(f'Part 2 answer: {part_2(self.day_6_data)}')  # 2472
