from game.action import Action

# TODO: Add your DrawActorsAction class here

class DrawActorsAction(Action):
    def __init__(self, output_service) -> None:
        self._output_service = output_service

    def execute(self, cast):
        """"""
        marquee = cast["marquee"][0] # there's only one
        robot = cast["robot"][0] # there's only one
        artifacts = cast["artifact"]

        self._output_service.clear_screen()

        for artifact in artifacts:
            pos = artifact.get_position()
            self._output_service.draw_text(pos.get_x(), pos.get_y(), artifact.get_text(), True)

        self._output_service.draw_text(robot.get_position().get_x(), robot.get_position().get_y(), robot.get_text(), True)
        self._output_service.draw_text(marquee.get_position().get_x(), marquee.get_position().get_y(), marquee.get_text(), True)
        
        self._output_service.flush_buffer()

