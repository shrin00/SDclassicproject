<%-- 
    Document   : customerlog.jsp
    Created on : Jun 29, 2019, 2:54:51 PM
    Author     : Srini-w10
--%>
<%
    if(request.getSession().getAttribute("accno")!=null)
    {
        response.sendRedirect("custhome.jsp");
    }
%>


 
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Customer-Login</title>

  <!-- Bootstrap -->
  <link href="assets/css/bootstrap.css" rel="stylesheet">
  <link href="assets/css/bootstrap-theme.css" rel="stylesheet">

  <!-- siimple style -->
  <link href="assets/css/style.css" rel="stylesheet">

  <!-- =======================================================
    Theme Name: Siimple
    Theme URL: https://bootstrapmade.com/free-bootstrap-landing-page/
    Author: BootstrapMade
    Author URL: https://bootstrapmade.com
  ======================================================= -->
</head>

<body>

  <!-- Fixed navbar -->
  <div class="navbar navbar-inverse navbar-fixed-top">
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        <a class="navbar-brand" href="index.html">Customer Login</a>
      </div>
      <div class="navbar-collapse collapse">
        <ul class="nav navbar-nav navbar-right">
          <li><a href="#"></a></li>
          <li><a href="#">Get in To Explore</a></li>
        </ul>
      </div>
      <!--/.nav-collapse -->
    </div>
  </div>

  <div id="header">
    <div class="container">
      <div class="row">
        <div class="col-lg-6">
          <h1>Easy Citizen Services</h1>
          <h2 class="subtitle">It's good you are on customer login page</h2>
          <form class="form-inline signup" action="custlog.jsp">
            <div class="form-group">
              <input type="text" class="form-control" name="accno" placeholder="Enter your account number">
            </div>
            <div class="form-group">
              <input type="password" class="form-control" name="pass" placeholder="Enter your account password">
            </div>
            <button type="submit" class="btn btn-theme">Login</button
            
          </form>
        </div>
        <div class="col-lg-4 col-lg-offset-2">
          <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
              <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
              <li data-target="#carousel-example-generic" data-slide-to="1"></li>
              <li data-target="#carousel-example-generic" data-slide-to="2"></li>
            </ol>
            <!-- slides -->
            <div class="carousel-inner">
              <div class="item active">
                <img src="ecs_logo.png" alt="" width="350" height="450">
              </div>
              <div class="item">
                <img src="assets/img/Logo-1561699162861.png" alt="" width="350" height="450">
              </div>
             
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
  <div id="footer">
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <p class="copyright">&copy; ECS PVT.LTD</p>
        </div>
        <div class="col-md-6">
          <div class="credits">
            <!--
              All the links in the footer should remain intact.
              You can delete the links only if you purchased the pro version.
              Licensing information: https://bootstrapmade.com/license/
              Purchase the pro version with working PHP/AJAX contact form: https://bootstrapmade.com/buy/?theme=Siimple
            -->
            Designed by <a href="https://bootstrapmade.com/">ECS</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
  <script src="assets/js/bootstrap.min.js"></script>
<a href="index.html">Go To Home Page</a>
</body>

</html>
