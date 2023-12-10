#!/usr/bin/python3
        """prints names in the compiled module"""
        import hidden_4

        if __name__ == "__main__":

                file = dir(hidden_4)
                for name in file:
                if name[:2] !+ "--":
                print(file)
