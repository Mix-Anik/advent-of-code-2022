import logging

from inputs import get_file_data
from days.day_5 import part_1, part_2


LOG = logging.getLogger()


class TestDay5Solutions:

    def setup_class(self):
        self.test_day_5_data = get_file_data('input_day5_test', False)
        self.day_5_data = get_file_data('input_day5', False)

    def test_part_1(self):
        assert part_1(self.test_day_5_data) == 'CMZ'

    def test_part_2(self):
        assert part_2(self.test_day_5_data) == 'MCD'

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_5_data)}')  # ZRLJGSCTR
        LOG.info(f'Part 2 answer: {part_2(self.day_5_data)}')  # PRTTGRFPB
