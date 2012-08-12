'''
Created on Aug 12, 2012
Routines to test for MySQL access, data in/out of TestValDb
and NumPy, SciPy functionality
@author: dpollard2
'''


def test_numpy():
    ''' Trivial test of Numpy functionality to check it's there'''
    import numpy as np
    ary = np.arange(10).reshape(2,5)
    b= 3 * ary
    print "ary is", ary
    print "Info about array: shape", ary.shape, "Dimensions ", ary.ndim, "Type ", ary.dtype.name, "Size ", ary.size
    print "b is", b
    return None


def test_scipy():
    ''' Test SciPy functionality is available and use graph'''
    import numpy as np
    from scipy.interpolate import Rbf, InterpolatedUnivariateSpline
    import matplotlib
#    matplotlib.use('Agg')
    matplotlib.use('macosx')    #This is the correct matplotlib backend for Macs
    import matplotlib.pyplot as plt
    
    # setup data
    x = np.linspace(0, 10, 9)
    y = np.sin(x)
    xi = np.linspace(0, 10, 101)
    
    # use fitpack2 method
    ius = InterpolatedUnivariateSpline(x, y)
    yi = ius(xi)
    
    plt.subplot(2, 1, 1)
    plt.plot(x, y, 'bo')
    plt.plot(xi, yi, 'g')
    plt.plot(xi, np.sin(xi), 'r')
    plt.title('Interpolation using univariate spline')
    
    # use RBF method
#    rbf = Rbf(x, y)
#    fi = rbf(xi)
    
    plt.subplot(2, 1, 2)
    plt.plot(x, y, 'bo')
    plt.plot(xi, yi, 'g')
    plt.plot(xi, np.sin(xi), 'r')
    plt.title('Interpolation using RBF - multiquadrics')
#    plt.show()
    plt.savefig('/Users/dpollard2/Python/rbf1d.png')
    return None


def test_mysql():
    '''Test connection to Mysql and select statement '''
    import MySQLdb
    
    try:
        conn = MySQLdb.connect (db = "TestValDb",
                                host = "localhost",
                                port = 3307,
                                user = "dpollard2",
                                passwd = "connect2mysql")
    except Exception, e:
        print "Cannot connect to server! %s" % e
#        sys.exit()
    else:
        print "Connected"
#        stmt= """
#                INSERT INTO value (assetID, datetime, valueTypeID, value) 
#                VALUES (11,'2012-03-22 12:00', 1, 66.60)
#                """
        stmt= """
                SELECT * FROM  value 
                ORDER BY assetID, datetime
                """
        csr = conn.cursor()
        try:
            csr.execute( stmt)
#            rcount = csr.rowcount
#            csr.close()
#            conn.commit()
#            print "No. rows added: %d" % rcount
            
            print "No. rows selected: %d" % csr.rowcount
            rows = csr.fetchall()
            for r in rows:
                print r
        except Exception, e:
            print "Error during select: %s" % e
            try:
                conn.rollback()
            except:
                pass
            csr.close()
    return None
