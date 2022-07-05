# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" MVC-Pattern. """

import sys
from PyQt5.QtWidgets import QApplication
from view.view import Window
from model.model import Model

__version__ = "0.0.1"
__author__ = "klaus.moser"


class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create an instance of 'QApplication'
    win = Window()
    win.show()  # Show the calculator's GUI
    c = Controller(Model(win), win)  # Create the controller incl. Model & GUI
    sys.exit(app.exec())  # Execute main loop
