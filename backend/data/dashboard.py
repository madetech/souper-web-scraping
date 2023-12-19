def get_counts(session: Session):
    with session:
        resultSet = session.query('Get *').all()
        print(resultSet)
        results = __format_count_output(resultSet)
    return results

def __format_count_output(results):
    """ Should look like this
    [[["Stage", "Count"],["Alpha", 250],["Beta", 420],["Live", 290]], [["Stage", "Count"],["Alpha", 37],["Beta", 60],["Live", 70]]]
        """
    return ""