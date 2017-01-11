# Multithreaded + multi-processing makefile for:
#    Darwin valdez.seos.uvic.ca 16.3.0 Darwin Kernel Version 16.3.0: Thu Nov 17 20:23:58 PST 2016; root:xnu-3789.31.2~1/RELEASE_X86_64 x86_64
# This makefile was generated automatically on
#    Wed Jan 11 11:01:34 PST 2017
# by the command:
# executed by:
#    jklymak@valdez.seos.uvic.ca:/Users/jklymak/Dropbox/Teaching/MITgcmExampleSteadyGauss/build


#
# OPTFILE="../build_options/darwin_brewgfortranmpi"
#
# BUILDDIR     : Directory where object files are written
# SOURCEDIRS   : Directories containing the source (.F) files
# INCLUDEDIRS  : Directories containing the header-source (.h) files
# EXEDIR       : Directory where executable that is generated is written
# EXECUTABLE   : Full path of executable binary
#
# CPP          : C-preprocessor command
# INCLUDES     : Directories searched for header files
# DEFINES      : Macro definitions for CPP
# MAKEDEPEND   : Dependency generator
# FC           : Fortran compiler command
# FFLAGS       : Configuration/debugging options for FC
# FOPTIM       : Optimization options for FC
# LINK         : Command for link editor program
# LIBS         : Library flags /or/ additional optimization/debugging flags

ROOTDIR     = /Users/jklymak/MITgcmc66b/MITgcm
BUILDDIR    = .
SOURCEDIRS  =  ../code/ /Users/jklymak/MITgcmc66b/MITgcm/pkg/debug /Users/jklymak/MITgcmc66b/MITgcm/pkg/diagnostics /Users/jklymak/MITgcmc66b/MITgcm/pkg/generic_advdiff /Users/jklymak/MITgcmc66b/MITgcm/pkg/kl10 /Users/jklymak/MITgcmc66b/MITgcm/pkg/mdsio /Users/jklymak/MITgcmc66b/MITgcm/pkg/mom_common /Users/jklymak/MITgcmc66b/MITgcm/pkg/mom_fluxform /Users/jklymak/MITgcmc66b/MITgcm/pkg/mom_vecinv /Users/jklymak/MITgcmc66b/MITgcm/pkg/monitor /Users/jklymak/MITgcmc66b/MITgcm/pkg/obcs /Users/jklymak/MITgcmc66b/MITgcm/pkg/rw /Users/jklymak/MITgcmc66b/MITgcm/pkg/timeave /Users/jklymak/MITgcmc66b/MITgcm/eesupp/src /Users/jklymak/MITgcmc66b/MITgcm/model/src
INCLUDEDIRS =  ../code/ /Users/jklymak/MITgcmc66b/MITgcm/pkg/debug /Users/jklymak/MITgcmc66b/MITgcm/pkg/diagnostics /Users/jklymak/MITgcmc66b/MITgcm/pkg/generic_advdiff /Users/jklymak/MITgcmc66b/MITgcm/pkg/kl10 /Users/jklymak/MITgcmc66b/MITgcm/pkg/mdsio /Users/jklymak/MITgcmc66b/MITgcm/pkg/mom_common /Users/jklymak/MITgcmc66b/MITgcm/pkg/mom_fluxform /Users/jklymak/MITgcmc66b/MITgcm/pkg/mom_vecinv /Users/jklymak/MITgcmc66b/MITgcm/pkg/monitor /Users/jklymak/MITgcmc66b/MITgcm/pkg/obcs /Users/jklymak/MITgcmc66b/MITgcm/pkg/rw /Users/jklymak/MITgcmc66b/MITgcm/pkg/timeave /Users/jklymak/MITgcmc66b/MITgcm/eesupp/inc /Users/jklymak/MITgcmc66b/MITgcm/model/inc
EXEDIR      = .
EXECUTABLE  = $(EXEDIR)/mitgcmuv
TOOLSDIR    = /Users/jklymak/MITgcmc66b/MITgcm/tools
OADTOOLS    = 

#eh3  new defines for the adjoint work
AUTODIFF    = /Users/jklymak/MITgcmc66b/MITgcm/pkg/autodiff
EXE_AD      = mitgcmuv_ad
EXE_FTL     = mitgcmuv_ftl
EXE_SVD     = mitgcmuv_svd

ENABLED_PACKAGES =  -DALLOW_DEBUG -DALLOW_DIAGNOSTICS -DALLOW_GENERIC_ADVDIFF -DALLOW_KL10 -DALLOW_MDSIO -DALLOW_MOM_COMMON -DALLOW_MOM_FLUXFORM -DALLOW_MOM_VECINV -DALLOW_MONITOR -DALLOW_OBCS -DALLOW_RW -DALLOW_TIMEAVE
DISABLED_PACKAGES =  -UALLOW_ADMTLM -UALLOW_AIM_V23 -UALLOW_ATM2D -UALLOW_ATM_COMMON -UALLOW_ATM_COMPON_INTERF -UALLOW_ATM_OCN_COUPLER -UALLOW_ATM_PHYS -UALLOW_AUTODIFF -UALLOW_BBL -UALLOW_BLING -UALLOW_BULK_FORCE -UALLOW_CAL -UALLOW_CD_CODE -UALLOW_CFC -UALLOW_CHEAPAML -UALLOW_CHRONOS -UALLOW_COMPON_COMMUNIC -UALLOW_COST -UALLOW_CTRL -UALLOW_DIC -UALLOW_DOWN_SLOPE -UALLOW_EBM -UALLOW_ECCO -UALLOW_EMBED_FILES -UALLOW_EXCH2 -UALLOW_EXF -UALLOW_FIZHI -UALLOW_FLT -UALLOW_FRAZIL -UALLOW_GCHEM -UALLOW_GGL90 -UALLOW_GMREDI -UALLOW_GRDCHK -UALLOW_GRIDALT -UALLOW_ICEFRONT -UALLOW_KPP -UALLOW_LAND -UALLOW_LAYERS -UALLOW_LONGSTEP -UALLOW_MATRIX -UALLOW_MNC -UALLOW_MY82 -UALLOW_MYPACKAGE -UALLOW_OCN_COMPON_INTERF -UALLOW_OFFLINE -UALLOW_OPENAD -UALLOW_OPPS -UALLOW_PP81 -UALLOW_PROFILES -UALLOW_PTRACERS -UALLOW_RBCS -UALLOW_REGRID -UALLOW_RUNCLOCK -UALLOW_SALT_PLUME -UALLOW_SBO -UALLOW_SEAICE -UALLOW_SHAP_FILT -UALLOW_SHELFICE -UALLOW_SHOWFLOPS -UALLOW_SMOOTH -UALLOW_SPHERE -UALLOW_STREAMICE -UALLOW_THSICE -UALLOW_ZONAL_FILT

# These files are created by Makefile
SPECIAL_FILES = PACKAGES_CONFIG.h AD_CONFIG.h FC_NAMEMANGLE.h BUILD_INFO.h
EMBEDDED_FILES = 
# Unix ln (link)
LN = ln -s
# Dependency generator
MAKEDEPEND = makedepend
# Special preprocessor (KAP on DECs, FPP on Crays)
KPP = 
# Fortran compiler
FC = mpif90
# Fortran compiler
F90C = 
# C compiler
CC = mpicc
# Link editor
LINK = mpif90 

# Defines for CPP
DEFINES = -DWORDLENGTH=4 -DALWAYS_USE_MPI -DALLOW_USE_MPI -DHAVE_SYSTEM -DHAVE_FDATE -DHAVE_ETIME_SBR -DHAVE_CLOC -DHAVE_SETRLSTK -DHAVE_STAT -DHAVE_NETCDF -DHAVE_FLUSH 
# Includes for CPP
INCLUDES = -I. 
# default CPP includes for makedepend
CPPINCLUDES =  -I/usr/local/lib/gcc/x86_64-apple-darwin15.6.0/6.3.0/include -I/usr/local/include -I/usr/local/lib/gcc/x86_64-apple-darwin15.6.0/6.3.0/include-fixed -I/usr/include -I/System/Library/Frameworks -I/Library/Frameworks
# Flags for KPP
KFLAGS1 = 
KFLAGS2 = 
# Optim./debug for FC
FFLAGS = -Wunused -Wuninitialized 
FOPTIM = -O3 -funroll-loops -ftree-vectorize -ffpe-trap=invalid 
# Optim./debug for FC
F90FLAGS = 
F90OPTIM = 
F90FIXEDFORMAT = 
# Flags for CC
CFLAGS = 
# Files that should not be optimized
NOOPTFILES = 
NOOPTFLAGS = -O0
# Flags and libraries needed for linking
LIBS =  -lnetcdff -lnetcdf
# Name of the makefile
MAKEFILE = Makefile
# Name of the make program
MAKE = make

F77_SRC_FILES =  \
 chksum_tiled.F \
 debug_call.F \
 debug_cs_corner_uv.F \
 debug_enter.F \
 debug_fld_stats_rl.F \
 debug_fld_stats_rs.F \
 debug_leave.F \
 debug_msg.F \
 debug_stats_rl.F \
 debug_stats_rs.F \
 fill_in_corners_rl.F \
 write_fullarray_rl.F \
 write_fullarray_rs.F \
 diag_calc_psivel.F \
 diag_cg2d.F \
 diag_vegtile_fill.F \
 diagnostics_addtolist.F \
 diagnostics_calc_phivel.F \
 diagnostics_check.F \
 diagnostics_clear.F \
 diagnostics_fill.F \
 diagnostics_fill_field.F \
 diagnostics_fill_rs.F \
 diagnostics_fill_state.F \
 diagnostics_fract_fill.F \
 diagnostics_init_early.F \
 diagnostics_init_fixed.F \
 diagnostics_init_varia.F \
 diagnostics_interp_p2p.F \
 diagnostics_interp_vert.F \
 diagnostics_is_on.F \
 diagnostics_list_check.F \
 diagnostics_main_init.F \
 diagnostics_mnc_out.F \
 diagnostics_out.F \
 diagnostics_read_pickup.F \
 diagnostics_readparms.F \
 diagnostics_scale_fill.F \
 diagnostics_scale_fill_rs.F \
 diagnostics_set_calc.F \
 diagnostics_set_levels.F \
 diagnostics_set_pointers.F \
 diagnostics_setdiag.F \
 diagnostics_status_error.F \
 diagnostics_sum_levels.F \
 diagnostics_summary.F \
 diagnostics_switch_onoff.F \
 diagnostics_utils.F \
 diagnostics_write.F \
 diagnostics_write_pickup.F \
 diagstats_ascii_out.F \
 diagstats_calc.F \
 diagstats_clear.F \
 diagstats_close_io.F \
 diagstats_fill.F \
 diagstats_global.F \
 diagstats_ini_io.F \
 diagstats_local.F \
 diagstats_mnc_out.F \
 diagstats_others_calc.F \
 diagstats_output.F \
 diagstats_set_pointers.F \
 diagstats_set_regions.F \
 diagstats_setdiag.F \
 gad_advection.F \
 gad_advscheme.F \
 gad_biharm_r.F \
 gad_biharm_x.F \
 gad_biharm_y.F \
 gad_c2_adv_r.F \
 gad_c2_adv_x.F \
 gad_c2_adv_y.F \
 gad_c2_impl_r.F \
 gad_c4_adv_r.F \
 gad_c4_adv_x.F \
 gad_c4_adv_y.F \
 gad_calc_rhs.F \
 gad_check.F \
 gad_del2.F \
 gad_diagnostics_init.F \
 gad_diagnostics_state.F \
 gad_diff_r.F \
 gad_diff_x.F \
 gad_diff_y.F \
 gad_dst2u1_adv_r.F \
 gad_dst2u1_adv_x.F \
 gad_dst2u1_adv_y.F \
 gad_dst2u1_impl_r.F \
 gad_dst3_adv_r.F \
 gad_dst3_adv_x.F \
 gad_dst3_adv_y.F \
 gad_dst3fl_adv_r.F \
 gad_dst3fl_adv_x.F \
 gad_dst3fl_adv_y.F \
 gad_dst3fl_impl_r.F \
 gad_exch_som.F \
 gad_fluxlimit_adv_r.F \
 gad_fluxlimit_adv_x.F \
 gad_fluxlimit_adv_y.F \
 gad_fluxlimit_impl_r.F \
 gad_grad_x.F \
 gad_grad_y.F \
 gad_implicit_r.F \
 gad_init_fixed.F \
 gad_init_varia.F \
 gad_os7mp_adv_r.F \
 gad_os7mp_adv_x.F \
 gad_os7mp_adv_y.F \
 gad_osc_hat_r.F \
 gad_osc_hat_x.F \
 gad_osc_hat_y.F \
 gad_osc_mul_r.F \
 gad_osc_mul_x.F \
 gad_osc_mul_y.F \
 gad_plm_fun.F \
 gad_ppm_adv_r.F \
 gad_ppm_adv_x.F \
 gad_ppm_adv_y.F \
 gad_ppm_flx_r.F \
 gad_ppm_flx_x.F \
 gad_ppm_flx_y.F \
 gad_ppm_fun.F \
 gad_ppm_hat_r.F \
 gad_ppm_hat_x.F \
 gad_ppm_hat_y.F \
 gad_ppm_p3e_r.F \
 gad_ppm_p3e_x.F \
 gad_ppm_p3e_y.F \
 gad_pqm_adv_r.F \
 gad_pqm_adv_x.F \
 gad_pqm_adv_y.F \
 gad_pqm_flx_r.F \
 gad_pqm_flx_x.F \
 gad_pqm_flx_y.F \
 gad_pqm_fun.F \
 gad_pqm_hat_r.F \
 gad_pqm_hat_x.F \
 gad_pqm_hat_y.F \
 gad_pqm_p5e_r.F \
 gad_pqm_p5e_x.F \
 gad_pqm_p5e_y.F \
 gad_read_pickup.F \
 gad_som_adv_r.F \
 gad_som_adv_x.F \
 gad_som_adv_y.F \
 gad_som_advect.F \
 gad_som_exchanges.F \
 gad_som_fill_cs_corner.F \
 gad_som_lim_r.F \
 gad_som_prep_cs_corner.F \
 gad_u3_adv_r.F \
 gad_u3_adv_x.F \
 gad_u3_adv_y.F \
 gad_u3c4_impl_r.F \
 gad_write_pickup.F \
 salt_fill.F \
 kl10_calc.F \
 kl10_calc_diff.F \
 kl10_calc_visc.F \
 kl10_check.F \
 kl10_diagnostics_init.F \
 kl10_init_fixed.F \
 kl10_init_varia.F \
 kl10_output.F \
 kl10_readparms.F \
 mdsio_buffertorl.F \
 mdsio_buffertors.F \
 mdsio_check4file.F \
 mdsio_facef_read.F \
 mdsio_gl.F \
 mdsio_gl_slice.F \
 mdsio_pass_r4torl.F \
 mdsio_pass_r4tors.F \
 mdsio_pass_r8torl.F \
 mdsio_pass_r8tors.F \
 mdsio_rd_rec_rl.F \
 mdsio_rd_rec_rs.F \
 mdsio_read_field.F \
 mdsio_read_meta.F \
 mdsio_read_section.F \
 mdsio_read_tape.F \
 mdsio_read_whalos.F \
 mdsio_readvec_loc.F \
 mdsio_rw_field.F \
 mdsio_rw_slice.F \
 mdsio_seg4torl.F \
 mdsio_seg4tors.F \
 mdsio_seg8torl.F \
 mdsio_seg8tors.F \
 mdsio_segxtorx_2d.F \
 mdsio_wr_metafiles.F \
 mdsio_wr_rec_rl.F \
 mdsio_wr_rec_rs.F \
 mdsio_write_field.F \
 mdsio_write_meta.F \
 mdsio_write_section.F \
 mdsio_write_tape.F \
 mdsio_write_whalos.F \
 mdsio_writelocal.F \
 mdsio_writevec_loc.F \
 mom_calc_3d_strain.F \
 mom_calc_absvort3.F \
 mom_calc_hdiv.F \
 mom_calc_hfacz.F \
 mom_calc_ke.F \
 mom_calc_relvort3.F \
 mom_calc_smag_3d.F \
 mom_calc_strain.F \
 mom_calc_tension.F \
 mom_calc_visc.F \
 mom_diagnostics_init.F \
 mom_hdissip.F \
 mom_init_fixed.F \
 mom_quasihydrostatic.F \
 mom_u_botdrag_impl.F \
 mom_u_bottomdrag.F \
 mom_u_coriolis_nh.F \
 mom_u_implicit_r.F \
 mom_u_metric_nh.F \
 mom_u_rviscflux.F \
 mom_u_sidedrag.F \
 mom_uv_smag_3d.F \
 mom_v_botdrag_impl.F \
 mom_v_bottomdrag.F \
 mom_v_coriolis_nh.F \
 mom_v_implicit_r.F \
 mom_v_metric_nh.F \
 mom_v_rviscflux.F \
 mom_v_sidedrag.F \
 mom_w_coriolis_nh.F \
 mom_w_metric_nh.F \
 mom_w_sidedrag.F \
 mom_w_smag_3d.F \
 mom_calc_rtrans.F \
 mom_fluxform.F \
 mom_u_adv_uu.F \
 mom_u_adv_vu.F \
 mom_u_adv_wu.F \
 mom_u_coriolis.F \
 mom_u_del2u.F \
 mom_u_metric_cylinder.F \
 mom_u_metric_sphere.F \
 mom_u_xviscflux.F \
 mom_u_yviscflux.F \
 mom_uv_boundary.F \
 mom_v_adv_uv.F \
 mom_v_adv_vv.F \
 mom_v_adv_wv.F \
 mom_v_coriolis.F \
 mom_v_del2v.F \
 mom_v_metric_cylinder.F \
 mom_v_metric_sphere.F \
 mom_v_xviscflux.F \
 mom_v_yviscflux.F \
 mom_vecinv.F \
 mom_vi_coriolis.F \
 mom_vi_del2uv.F \
 mom_vi_hdissip.F \
 mom_vi_u_coriolis.F \
 mom_vi_u_coriolis_c4.F \
 mom_vi_u_grad_ke.F \
 mom_vi_u_vertshear.F \
 mom_vi_v_coriolis.F \
 mom_vi_v_coriolis_c4.F \
 mom_vi_v_grad_ke.F \
 mom_vi_v_vertshear.F \
 mon_advcfl.F \
 mon_advcflw.F \
 mon_advcflw2.F \
 mon_calc_advcfl.F \
 mon_calc_stats_rl.F \
 mon_calc_stats_rs.F \
 mon_init.F \
 mon_ke.F \
 mon_out.F \
 mon_printstats_rl.F \
 mon_printstats_rs.F \
 mon_set_iounit.F \
 mon_set_pref.F \
 mon_solution.F \
 mon_stats_latbnd_rl.F \
 mon_stats_rl.F \
 mon_stats_rs.F \
 mon_surfcor.F \
 mon_vort3.F \
 mon_writestats_rl.F \
 mon_writestats_rs.F \
 monitor.F \
 monitor_ad.F \
 monitor_g.F \
 obcs_add_tides.F \
 obcs_adjust_uvice.F \
 obcs_apply_eta.F \
 obcs_apply_ptracer.F \
 obcs_apply_r_star.F \
 obcs_apply_seaice.F \
 obcs_apply_surf_dr.F \
 obcs_apply_ts.F \
 obcs_apply_uv.F \
 obcs_apply_uvice.F \
 obcs_apply_w.F \
 obcs_balance_flow.F \
 obcs_calc.F \
 obcs_calc_stevens.F \
 obcs_check.F \
 obcs_check_depths.F \
 obcs_copy_tracer.F \
 obcs_copy_uv_n.F \
 obcs_diag_balance.F \
 obcs_exchanges.F \
 obcs_exf_load.F \
 obcs_fields_load.F \
 obcs_init_fixed.F \
 obcs_init_variables.F \
 obcs_mon_stats.F \
 obcs_monitor.F \
 obcs_output.F \
 obcs_prescribe_read.F \
 obcs_read_pickup.F \
 obcs_readparms.F \
 obcs_save_uv_n.F \
 obcs_seaice_sponge.F \
 obcs_set_connect.F \
 obcs_sponge.F \
 obcs_u1_adv_tracer.F \
 obcs_write_pickup.F \
 orlanski_east.F \
 orlanski_init.F \
 orlanski_north.F \
 orlanski_south.F \
 orlanski_west.F \
 get_write_global_fld.F \
 read_fld_xy_rl.F \
 read_fld_xy_rs.F \
 read_fld_xyz_rl.F \
 read_fld_xyz_rs.F \
 read_glvec_rl.F \
 read_glvec_rs.F \
 read_mflds.F \
 read_rec.F \
 set_write_global_fld.F \
 write_fld_3d_rl.F \
 write_fld_3d_rs.F \
 write_fld_s3d_rl.F \
 write_fld_s3d_rs.F \
 write_fld_xy_rl.F \
 write_fld_xy_rs.F \
 write_fld_xyz_rl.F \
 write_fld_xyz_rs.F \
 write_glvec_rl.F \
 write_glvec_rs.F \
 write_local_rl.F \
 write_local_rs.F \
 write_rec.F \
 timeave_cumul_1k1t.F \
 timeave_cumul_1t.F \
 timeave_cumul_1vfc.F \
 timeave_cumul_2v.F \
 timeave_cumul_2vfc.F \
 timeave_cumul_dif_1t.F \
 timeave_cumulate.F \
 timeave_init_fixed.F \
 timeave_norma_2v.F \
 timeave_normalize.F \
 timeave_reset.F \
 timeave_statv_write.F \
 timeave_statvars.F \
 timeave_surf_flux.F \
 all_proc_die.F \
 bar2.F \
 bar_check.F \
 barrier.F \
 check_threads.F \
 comm_stats.F \
 cumulsum_z_tile.F \
 diff_phase_multiple.F \
 different_multiple.F \
 eeboot.F \
 eeboot_minimal.F \
 eedata_example.F \
 eedie.F \
 eeintro_msg.F \
 eeset_parms.F \
 eewrite_eeenv.F \
 exch0_r4.F \
 exch0_r8.F \
 exch0_rl.F \
 exch0_rs.F \
 exch1_bg_r4_cube.F \
 exch1_bg_r8_cube.F \
 exch1_bg_rl_cube.F \
 exch1_bg_rs_cube.F \
 exch1_r4.F \
 exch1_r4_cube.F \
 exch1_r8.F \
 exch1_r8_cube.F \
 exch1_rl.F \
 exch1_rl_ad.F \
 exch1_rl_cube.F \
 exch1_rl_cube_ad.F \
 exch1_rs.F \
 exch1_rs_ad.F \
 exch1_rs_cube.F \
 exch1_rs_cube_ad.F \
 exch1_uv_r4_cube.F \
 exch1_uv_r8_cube.F \
 exch1_uv_rl_cube.F \
 exch1_uv_rs_cube.F \
 exch1_z_r4_cube.F \
 exch1_z_r8_cube.F \
 exch1_z_rl_cube.F \
 exch1_z_rs_cube.F \
 exch_3d_r4.F \
 exch_3d_r8.F \
 exch_3d_rl.F \
 exch_3d_rs.F \
 exch_cycle_ebl.F \
 exch_init.F \
 exch_r4_recv_get_x.F \
 exch_r4_recv_get_y.F \
 exch_r4_send_put_x.F \
 exch_r4_send_put_y.F \
 exch_r8_recv_get_x.F \
 exch_r8_recv_get_y.F \
 exch_r8_send_put_x.F \
 exch_r8_send_put_y.F \
 exch_rl_recv_get_x.F \
 exch_rl_recv_get_y.F \
 exch_rl_send_put_x.F \
 exch_rl_send_put_y.F \
 exch_rs_recv_get_x.F \
 exch_rs_recv_get_y.F \
 exch_rs_send_put_x.F \
 exch_rs_send_put_y.F \
 exch_s3d_r4.F \
 exch_s3d_r8.F \
 exch_s3d_rl.F \
 exch_s3d_rs.F \
 exch_sm_3d_r4.F \
 exch_sm_3d_r8.F \
 exch_sm_3d_rl.F \
 exch_sm_3d_rs.F \
 exch_uv_3d_r4.F \
 exch_uv_3d_r8.F \
 exch_uv_3d_rl.F \
 exch_uv_3d_rs.F \
 exch_uv_agrid_3d_r4.F \
 exch_uv_agrid_3d_r8.F \
 exch_uv_agrid_3d_rl.F \
 exch_uv_agrid_3d_rs.F \
 exch_uv_bgrid_3d_r4.F \
 exch_uv_bgrid_3d_r8.F \
 exch_uv_bgrid_3d_rl.F \
 exch_uv_bgrid_3d_rs.F \
 exch_uv_dgrid_3d_r4.F \
 exch_uv_dgrid_3d_r8.F \
 exch_uv_dgrid_3d_rl.F \
 exch_uv_dgrid_3d_rs.F \
 exch_uv_xy_r4.F \
 exch_uv_xy_r8.F \
 exch_uv_xy_rl.F \
 exch_uv_xy_rs.F \
 exch_uv_xyz_r4.F \
 exch_uv_xyz_r8.F \
 exch_uv_xyz_rl.F \
 exch_uv_xyz_rs.F \
 exch_xy_r4.F \
 exch_xy_r8.F \
 exch_xy_rl.F \
 exch_xy_rs.F \
 exch_xyz_r4.F \
 exch_xyz_r8.F \
 exch_xyz_rl.F \
 exch_xyz_rs.F \
 exch_z_3d_r4.F \
 exch_z_3d_r8.F \
 exch_z_3d_rl.F \
 exch_z_3d_rs.F \
 fill_cs_corner_ag_rl.F \
 fill_cs_corner_tr_rl.F \
 fill_cs_corner_uv_rl.F \
 fill_cs_corner_uv_rs.F \
 fool_the_compiler.F \
 gather_2d_r4.F \
 gather_2d_r8.F \
 gather_2d_wh_r4.F \
 gather_2d_wh_r8.F \
 gather_vec_r4.F \
 gather_vec_r8.F \
 gather_xz.F \
 gather_yz.F \
 get_periodic_interval.F \
 global_max.F \
 global_sum.F \
 global_sum_singlecpu.F \
 global_sum_tile.F \
 global_vec_sum.F \
 gsum.F \
 ini_communication_patterns.F \
 ini_procs.F \
 ini_threading_environment.F \
 lef_zero.F \
 main.F \
 master_cpu_io.F \
 master_cpu_thread.F \
 mds_byteswapi4.F \
 mds_byteswapr4.F \
 mds_byteswapr8.F \
 mds_flush.F \
 mds_reclen.F \
 mdsfindunit.F \
 memsync.F \
 nml_change_syntax.F \
 nml_set_terminator.F \
 open_copy_data_file.F \
 print.F \
 reset_halo.F \
 scatter_2d_r4.F \
 scatter_2d_r8.F \
 scatter_2d_wh_r4.F \
 scatter_2d_wh_r8.F \
 scatter_vec_r4.F \
 scatter_vec_r8.F \
 scatter_xz.F \
 scatter_yz.F \
 stop_if_error.F \
 timers.F \
 utils.F \
 write_utils.F \
 adams_bashforth2.F \
 adams_bashforth3.F \
 add_walls2masks.F \
 apply_forcing.F \
 calc_3d_diffusivity.F \
 calc_adv_flow.F \
 calc_div_ghat.F \
 calc_eddy_stress.F \
 calc_grad_phi_fv.F \
 calc_grad_phi_hyd.F \
 calc_grad_phi_surf.F \
 calc_grid_angles.F \
 calc_gw.F \
 calc_ivdc.F \
 calc_oce_mxlayer.F \
 calc_phi_hyd.F \
 calc_r_star.F \
 calc_surf_dr.F \
 calc_viscosity.F \
 calc_wsurf_tr.F \
 cg2d.F \
 cg2d_ex0.F \
 cg2d_nsa.F \
 cg2d_sr.F \
 cg3d.F \
 cg3d_ex0.F \
 check_pickup.F \
 config_check.F \
 config_summary.F \
 convective_adjustment.F \
 convective_adjustment_ini.F \
 convective_weights.F \
 convectively_mixtracer.F \
 correction_step.F \
 cycle_ab_tracer.F \
 cycle_tracer.F \
 diags_oceanic_surf_flux.F \
 diags_phi_hyd.F \
 diags_phi_rlow.F \
 diags_rho.F \
 do_atmospheric_phys.F \
 do_fields_blocking_exchanges.F \
 do_oceanic_phys.F \
 do_stagger_fields_exchanges.F \
 do_statevars_diags.F \
 do_statevars_tave.F \
 do_the_model_io.F \
 do_write_pickup.F \
 dynamics.F \
 external_fields_load.F \
 external_forcing.F \
 external_forcing_surf.F \
 find_alpha.F \
 find_hyd_press_1d.F \
 find_rho.F \
 forcing_surf_relax.F \
 forward_step.F \
 freesurf_rescale_g.F \
 freeze_surface.F \
 grad_sigma.F \
 gsw_teos10.F \
 impldiff.F \
 ini_cartesian_grid.F \
 ini_cg2d.F \
 ini_cg3d.F \
 ini_cori.F \
 ini_curvilinear_grid.F \
 ini_cylinder_grid.F \
 ini_depths.F \
 ini_dynvars.F \
 ini_eos.F \
 ini_ffields.F \
 ini_fields.F \
 ini_forcing.F \
 ini_global_domain.F \
 ini_grid.F \
 ini_linear_phisurf.F \
 ini_local_grid.F \
 ini_masks_etc.F \
 ini_mixing.F \
 ini_mnc_vars.F \
 ini_model_io.F \
 ini_nh_fields.F \
 ini_nh_vars.F \
 ini_nlfs_vars.F \
 ini_p_ground.F \
 ini_parms.F \
 ini_pressure.F \
 ini_psurf.F \
 ini_salt.F \
 ini_sigma_hfac.F \
 ini_spherical_polar_grid.F \
 ini_theta.F \
 ini_vel.F \
 ini_vertical_grid.F \
 initialise_fixed.F \
 initialise_varia.F \
 integr_continuity.F \
 integrate_for_w.F \
 load_fields_driver.F \
 load_grid_spacing.F \
 load_ref_files.F \
 main_do_loop.F \
 momentum_correction_step.F \
 packages_boot.F \
 packages_check.F \
 packages_error_msg.F \
 packages_init_fixed.F \
 packages_init_variables.F \
 packages_print_msg.F \
 packages_readparms.F \
 packages_unused_msg.F \
 packages_write_pickup.F \
 plot_field.F \
 port_rand.F \
 post_cg3d.F \
 pre_cg3d.F \
 pressure_for_eos.F \
 read_pickup.F \
 remove_mean.F \
 reset_nlfs_vars.F \
 rotate_spherical_polar_grid.F \
 rotate_uv2en.F \
 salt_integrate.F \
 seawater.F \
 set_defaults.F \
 set_grid_factors.F \
 set_parms.F \
 set_ref_state.F \
 solve_for_pressure.F \
 solve_pentadiagonal.F \
 solve_tridiagonal.F \
 solve_uv_tridiago.F \
 state_summary.F \
 swfrac.F \
 taueddy_init_varia.F \
 taueddy_tendency_apply.F \
 temp_integrate.F \
 the_main_loop.F \
 the_model_main.F \
 thermodynamics.F \
 timestep.F \
 timestep_tracer.F \
 timestep_wvel.F \
 tracers_correction_step.F \
 tracers_iigw_correction.F \
 turnoff_model_io.F \
 update_cg2d.F \
 update_etah.F \
 update_etaws.F \
 update_masks_etc.F \
 update_r_star.F \
 update_sigma.F \
 update_surf_dr.F \
 write_grid.F \
 write_pickup.F \
 write_state.F
NON_AD_F77_SRC_FILES =  \
 chksum_tiled.F \
 debug_call.F \
 debug_cs_corner_uv.F \
 debug_enter.F \
 debug_fld_stats_rl.F \
 debug_fld_stats_rs.F \
 debug_leave.F \
 debug_msg.F \
 debug_stats_rl.F \
 debug_stats_rs.F \
 fill_in_corners_rl.F \
 write_fullarray_rl.F \
 write_fullarray_rs.F \
 diag_calc_psivel.F \
 diag_cg2d.F \
 diag_vegtile_fill.F \
 diagnostics_addtolist.F \
 diagnostics_calc_phivel.F \
 diagnostics_check.F \
 diagnostics_clear.F \
 diagnostics_fill.F \
 diagnostics_fill_field.F \
 diagnostics_fill_rs.F \
 diagnostics_fill_state.F \
 diagnostics_fract_fill.F \
 diagnostics_init_early.F \
 diagnostics_init_fixed.F \
 diagnostics_init_varia.F \
 diagnostics_interp_p2p.F \
 diagnostics_interp_vert.F \
 diagnostics_list_check.F \
 diagnostics_main_init.F \
 diagnostics_mnc_out.F \
 diagnostics_out.F \
 diagnostics_read_pickup.F \
 diagnostics_readparms.F \
 diagnostics_scale_fill.F \
 diagnostics_scale_fill_rs.F \
 diagnostics_set_calc.F \
 diagnostics_set_levels.F \
 diagnostics_set_pointers.F \
 diagnostics_setdiag.F \
 diagnostics_status_error.F \
 diagnostics_sum_levels.F \
 diagnostics_summary.F \
 diagnostics_switch_onoff.F \
 diagnostics_utils.F \
 diagnostics_write.F \
 diagnostics_write_pickup.F \
 diagstats_ascii_out.F \
 diagstats_calc.F \
 diagstats_clear.F \
 diagstats_close_io.F \
 diagstats_fill.F \
 diagstats_global.F \
 diagstats_ini_io.F \
 diagstats_local.F \
 diagstats_mnc_out.F \
 diagstats_others_calc.F \
 diagstats_output.F \
 diagstats_set_pointers.F \
 diagstats_set_regions.F \
 diagstats_setdiag.F \
 gad_advscheme.F \
 gad_check.F \
 gad_diagnostics_init.F \
 gad_diagnostics_state.F \
 gad_init_fixed.F \
 gad_osc_hat_r.F \
 gad_osc_hat_x.F \
 gad_osc_hat_y.F \
 gad_osc_mul_r.F \
 gad_osc_mul_x.F \
 gad_osc_mul_y.F \
 gad_plm_fun.F \
 gad_ppm_adv_r.F \
 gad_ppm_adv_x.F \
 gad_ppm_adv_y.F \
 gad_ppm_flx_r.F \
 gad_ppm_flx_x.F \
 gad_ppm_flx_y.F \
 gad_ppm_fun.F \
 gad_ppm_hat_r.F \
 gad_ppm_hat_x.F \
 gad_ppm_hat_y.F \
 gad_ppm_p3e_r.F \
 gad_ppm_p3e_x.F \
 gad_ppm_p3e_y.F \
 gad_pqm_adv_r.F \
 gad_pqm_adv_x.F \
 gad_pqm_adv_y.F \
 gad_pqm_flx_r.F \
 gad_pqm_flx_x.F \
 gad_pqm_flx_y.F \
 gad_pqm_fun.F \
 gad_pqm_hat_r.F \
 gad_pqm_hat_x.F \
 gad_pqm_hat_y.F \
 gad_pqm_p5e_r.F \
 gad_pqm_p5e_x.F \
 gad_pqm_p5e_y.F \
 gad_write_pickup.F \
 salt_fill.F \
 kl10_calc.F \
 kl10_calc_diff.F \
 kl10_calc_visc.F \
 kl10_check.F \
 kl10_diagnostics_init.F \
 kl10_init_fixed.F \
 kl10_init_varia.F \
 kl10_output.F \
 kl10_readparms.F \
 mdsio_buffertorl.F \
 mdsio_buffertors.F \
 mdsio_check4file.F \
 mdsio_facef_read.F \
 mdsio_gl.F \
 mdsio_gl_slice.F \
 mdsio_pass_r4torl.F \
 mdsio_pass_r4tors.F \
 mdsio_pass_r8torl.F \
 mdsio_pass_r8tors.F \
 mdsio_rd_rec_rl.F \
 mdsio_rd_rec_rs.F \
 mdsio_read_field.F \
 mdsio_read_meta.F \
 mdsio_read_section.F \
 mdsio_read_tape.F \
 mdsio_read_whalos.F \
 mdsio_readvec_loc.F \
 mdsio_rw_field.F \
 mdsio_rw_slice.F \
 mdsio_seg4torl.F \
 mdsio_seg4tors.F \
 mdsio_seg8torl.F \
 mdsio_seg8tors.F \
 mdsio_segxtorx_2d.F \
 mdsio_wr_metafiles.F \
 mdsio_wr_rec_rl.F \
 mdsio_wr_rec_rs.F \
 mdsio_write_field.F \
 mdsio_write_meta.F \
 mdsio_write_section.F \
 mdsio_write_tape.F \
 mdsio_write_whalos.F \
 mdsio_writelocal.F \
 mdsio_writevec_loc.F \
 mom_calc_3d_strain.F \
 mom_calc_smag_3d.F \
 mom_diagnostics_init.F \
 mom_init_fixed.F \
 mom_u_botdrag_impl.F \
 mom_u_implicit_r.F \
 mom_uv_smag_3d.F \
 mom_v_botdrag_impl.F \
 mom_v_implicit_r.F \
 mom_w_coriolis_nh.F \
 mom_w_metric_nh.F \
 mom_w_sidedrag.F \
 mom_w_smag_3d.F \
 mom_uv_boundary.F \
 mon_advcfl.F \
 mon_advcflw.F \
 mon_advcflw2.F \
 mon_calc_advcfl.F \
 mon_calc_stats_rl.F \
 mon_calc_stats_rs.F \
 mon_init.F \
 mon_ke.F \
 mon_out.F \
 mon_printstats_rl.F \
 mon_printstats_rs.F \
 mon_set_iounit.F \
 mon_set_pref.F \
 mon_solution.F \
 mon_stats_latbnd_rl.F \
 mon_stats_rl.F \
 mon_stats_rs.F \
 mon_surfcor.F \
 mon_vort3.F \
 mon_writestats_rl.F \
 mon_writestats_rs.F \
 monitor.F \
 monitor_ad.F \
 monitor_g.F \
 obcs_add_tides.F \
 obcs_check.F \
 obcs_check_depths.F \
 obcs_diag_balance.F \
 obcs_init_fixed.F \
 obcs_mon_stats.F \
 obcs_monitor.F \
 obcs_output.F \
 obcs_readparms.F \
 obcs_seaice_sponge.F \
 obcs_set_connect.F \
 obcs_write_pickup.F \
 get_write_global_fld.F \
 read_glvec_rl.F \
 read_glvec_rs.F \
 read_mflds.F \
 set_write_global_fld.F \
 write_fld_3d_rl.F \
 write_fld_3d_rs.F \
 write_fld_s3d_rl.F \
 write_fld_s3d_rs.F \
 write_fld_xy_rl.F \
 write_fld_xy_rs.F \
 write_fld_xyz_rl.F \
 write_fld_xyz_rs.F \
 write_glvec_rl.F \
 write_glvec_rs.F \
 write_local_rl.F \
 write_local_rs.F \
 write_rec.F \
 timeave_init_fixed.F \
 all_proc_die.F \
 bar2.F \
 bar_check.F \
 barrier.F \
 check_threads.F \
 comm_stats.F \
 cumulsum_z_tile.F \
 diff_phase_multiple.F \
 eeboot.F \
 eeboot_minimal.F \
 eedata_example.F \
 eedie.F \
 eeintro_msg.F \
 eeset_parms.F \
 eewrite_eeenv.F \
 exch0_r4.F \
 exch0_r8.F \
 exch0_rl.F \
 exch0_rs.F \
 exch1_bg_r4_cube.F \
 exch1_bg_r8_cube.F \
 exch1_bg_rl_cube.F \
 exch1_bg_rs_cube.F \
 exch1_r4.F \
 exch1_r4_cube.F \
 exch1_r8.F \
 exch1_r8_cube.F \
 exch1_rl.F \
 exch1_rl_ad.F \
 exch1_rl_cube.F \
 exch1_rl_cube_ad.F \
 exch1_rs.F \
 exch1_rs_ad.F \
 exch1_rs_cube.F \
 exch1_rs_cube_ad.F \
 exch1_uv_r4_cube.F \
 exch1_uv_r8_cube.F \
 exch1_uv_rl_cube.F \
 exch1_uv_rs_cube.F \
 exch1_z_r4_cube.F \
 exch1_z_r8_cube.F \
 exch1_z_rl_cube.F \
 exch1_z_rs_cube.F \
 exch_3d_r4.F \
 exch_3d_r8.F \
 exch_cycle_ebl.F \
 exch_init.F \
 exch_r4_recv_get_x.F \
 exch_r4_recv_get_y.F \
 exch_r4_send_put_x.F \
 exch_r4_send_put_y.F \
 exch_r8_recv_get_x.F \
 exch_r8_recv_get_y.F \
 exch_r8_send_put_x.F \
 exch_r8_send_put_y.F \
 exch_rl_recv_get_x.F \
 exch_rl_recv_get_y.F \
 exch_rl_send_put_x.F \
 exch_rl_send_put_y.F \
 exch_rs_recv_get_x.F \
 exch_rs_recv_get_y.F \
 exch_rs_send_put_x.F \
 exch_rs_send_put_y.F \
 exch_s3d_r4.F \
 exch_s3d_r8.F \
 exch_s3d_rl.F \
 exch_s3d_rs.F \
 exch_sm_3d_r4.F \
 exch_sm_3d_r8.F \
 exch_sm_3d_rs.F \
 exch_uv_3d_r4.F \
 exch_uv_3d_r8.F \
 exch_uv_agrid_3d_r4.F \
 exch_uv_agrid_3d_r8.F \
 exch_uv_bgrid_3d_r4.F \
 exch_uv_bgrid_3d_r8.F \
 exch_uv_bgrid_3d_rl.F \
 exch_uv_bgrid_3d_rs.F \
 exch_uv_dgrid_3d_r4.F \
 exch_uv_dgrid_3d_r8.F \
 exch_uv_xy_r4.F \
 exch_uv_xy_r8.F \
 exch_uv_xyz_r4.F \
 exch_uv_xyz_r8.F \
 exch_xy_r4.F \
 exch_xy_r8.F \
 exch_xyz_r4.F \
 exch_xyz_r8.F \
 exch_z_3d_r4.F \
 exch_z_3d_r8.F \
 exch_z_3d_rl.F \
 exch_z_3d_rs.F \
 fool_the_compiler.F \
 gather_2d_r4.F \
 gather_2d_r8.F \
 gather_2d_wh_r4.F \
 gather_2d_wh_r8.F \
 gather_vec_r4.F \
 gather_vec_r8.F \
 gather_xz.F \
 gather_yz.F \
 global_max.F \
 global_sum.F \
 global_sum_singlecpu.F \
 global_sum_tile.F \
 global_vec_sum.F \
 gsum.F \
 ini_communication_patterns.F \
 ini_procs.F \
 ini_threading_environment.F \
 main.F \
 master_cpu_io.F \
 master_cpu_thread.F \
 mds_byteswapi4.F \
 mds_byteswapr4.F \
 mds_byteswapr8.F \
 mds_flush.F \
 mds_reclen.F \
 mdsfindunit.F \
 memsync.F \
 nml_change_syntax.F \
 nml_set_terminator.F \
 open_copy_data_file.F \
 print.F \
 reset_halo.F \
 scatter_2d_r4.F \
 scatter_2d_r8.F \
 scatter_2d_wh_r4.F \
 scatter_2d_wh_r8.F \
 scatter_vec_r4.F \
 scatter_vec_r8.F \
 scatter_xz.F \
 scatter_yz.F \
 stop_if_error.F \
 timers.F \
 utils.F \
 write_utils.F \
 calc_eddy_stress.F \
 calc_grid_angles.F \
 calc_gw.F \
 calc_oce_mxlayer.F \
 cg2d.F \
 cg2d_ex0.F \
 cg2d_sr.F \
 cg3d.F \
 cg3d_ex0.F \
 check_pickup.F \
 config_check.F \
 config_summary.F \
 diags_oceanic_surf_flux.F \
 do_statevars_diags.F \
 do_statevars_tave.F \
 do_the_model_io.F \
 do_write_pickup.F \
 external_forcing.F \
 find_hyd_press_1d.F \
 gsw_teos10.F \
 ini_cg3d.F \
 ini_eos.F \
 ini_global_domain.F \
 ini_local_grid.F \
 ini_mnc_vars.F \
 ini_model_io.F \
 ini_nh_vars.F \
 ini_parms.F \
 initialise_fixed.F \
 load_ref_files.F \
 packages_boot.F \
 packages_check.F \
 packages_error_msg.F \
 packages_init_fixed.F \
 packages_print_msg.F \
 packages_readparms.F \
 packages_unused_msg.F \
 packages_write_pickup.F \
 plot_field.F \
 port_rand.F \
 post_cg3d.F \
 pre_cg3d.F \
 rotate_spherical_polar_grid.F \
 set_defaults.F \
 set_grid_factors.F \
 set_parms.F \
 set_ref_state.F \
 solve_uv_tridiago.F \
 the_model_main.F \
 timestep_wvel.F \
 tracers_iigw_correction.F \
 turnoff_model_io.F \
 write_grid.F \
 write_pickup.F \
 write_state.F
C_SRC_FILES =  \
 gsl_ieee_env.c \
 ptwrapper.c \
 setdir.c \
 setrlstk.c \
 sigreg.c \
 tim.c \
 timer_stats.c
F90_SRC_FILES = 
H_SRC_FILES =  \
 CPP_OPTIONS.h \
 SIZE.h \
 DEBUG_OPTIONS.h \
 DIAGNOSTICS.h \
 DIAGNOSTICS_CALC.h \
 DIAGNOSTICS_SIZE.h \
 DIAGSTATS_REGIONS.h \
 DIAG_OPTIONS.h \
 GAD.h \
 GAD_FLUX_LIMITER.h \
 GAD_OPTIONS.h \
 GAD_SOM_VARS.h \
 gad_ad_check_lev1_dir.h \
 gad_ad_check_lev2_dir.h \
 gad_ad_check_lev3_dir.h \
 gad_ad_check_lev4_dir.h \
 KL10.h \
 KL10_DIAGS.h \
 KL10_OPTIONS.h \
 KL10_TAVE.h \
 MDSIO_BUFF_3D.h \
 MDSIO_BUFF_WH.h \
 MDSIO_OPTIONS.h \
 MOM_COMMON_OPTIONS.h \
 MOM_VISC.h \
 MOM_FLUXFORM.h \
 MOM_FLUXFORM_OPTIONS.h \
 MOM_VECINV_OPTIONS.h \
 MONITOR.h \
 MONITOR_OPTIONS.h \
 OBCS_FIELDS.h \
 OBCS_GRID.h \
 OBCS_OPTIONS.h \
 OBCS_PARAMS.h \
 OBCS_PTRACERS.h \
 OBCS_SEAICE.h \
 ORLANSKI.h \
 obcs_ad_check_lev1_dir.h \
 obcs_ad_check_lev2_dir.h \
 obcs_ad_check_lev3_dir.h \
 obcs_ad_check_lev4_dir.h \
 RW_MFLDS.h \
 RW_OPTIONS.h \
 TIMEAVE_OPTIONS.h \
 TIMEAVE_STATV.h \
 BAR2.h \
 BARRIER.h \
 CPP_EEMACROS.h \
 CPP_EEOPTIONS.h \
 CUMULSUM.h \
 DEF_IN_MAKEFILE.h \
 EEBUFF_SCPU.h \
 EEPARAMS.h \
 EESUPPORT.h \
 EXCH.h \
 GLOBAL_MAX.h \
 GLOBAL_SUM.h \
 MAIN_PDIRECTIVES1.h \
 MAIN_PDIRECTIVES2.h \
 MPI_INFO.h \
 SIGREG.h \
 CG2D.h \
 CG3D.h \
 DXC_MACROS.h \
 DXF_MACROS.h \
 DXG_MACROS.h \
 DXV_MACROS.h \
 DYC_MACROS.h \
 DYF_MACROS.h \
 DYG_MACROS.h \
 DYNVARS.h \
 DYU_MACROS.h \
 EOS.h \
 FCORI_MACROS.h \
 FFIELDS.h \
 GRID.h \
 GRID_MACROS.h \
 HFACC_MACROS.h \
 HFACS_MACROS.h \
 HFACW_MACROS.h \
 MASKS_MACROS.h \
 MASKW_MACROS.h \
 NH_VARS.h \
 PARAMS.h \
 RAS_MACROS.h \
 RAW_MACROS.h \
 RA_MACROS.h \
 RECIP_DXC_MACROS.h \
 RECIP_DXF_MACROS.h \
 RECIP_DXG_MACROS.h \
 RECIP_DXV_MACROS.h \
 RECIP_DYC_MACROS.h \
 RECIP_DYF_MACROS.h \
 RECIP_DYG_MACROS.h \
 RECIP_DYU_MACROS.h \
 RECIP_HFACC_MACROS.h \
 RECIP_HFACS_MACROS.h \
 RECIP_HFACW_MACROS.h \
 RESTART.h \
 SET_GRID.h \
 SOLVE_FOR_PRESSURE.h \
 SOLVE_FOR_PRESSURE3D.h \
 SURFACE.h \
 TANPHIATU_MACROS.h \
 TANPHIATV_MACROS.h \
 THE_MODEL_COMMON_BLOCKS.h \
 XC_MACROS.h \
 YC_MACROS.h
AD_FLOW_FILES =  \
 debug_ad.flow \
 diagnostics_ad.flow \
 mdsio_ad.flow \
 monitor_ad.flow \
 obcs_ad.flow \
 rw_ad.flow \
 eesupp.flow \
 exch1_ad.flow

F77_PP_SRC_FILES = $(F77_SRC_FILES:.F=.for)
F90_PP_SRC_FILES = $(F90_SRC_FILES:.F90=.fr9)
OBJFILES= $(F77_SRC_FILES:.F=.o) $(C_SRC_FILES:.c=.o) $(F90_SRC_FILES:.F90=.o)
FLOWFILES =  $(AD_FLOW_FILES:.flow=.flowdir)

.SUFFIXES:
.SUFFIXES: .o .for .p .F .c .ffr9 .fr9 .FF90 .F90 .flowdir .flow

all: fwd_exe_target
fwd_exe_target:
	@echo Update AD_CONFIG.h and make $(EXECUTABLE)
	@$(TOOLSDIR)/convert_cpp_cmd2defines "Forward version" -bAD_CONFIG_H -UALLOW_ADJOINT_RUN -UALLOW_TANGENTLINEAR_RUN > ad_config.template
	@cmp ad_config.template AD_CONFIG.h || cat ad_config.template > AD_CONFIG.h
	@-rm -f ad_config.template
	$(MAKE) -f $(MAKEFILE) $(EXECUTABLE)

$(EXECUTABLE): $(SPECIAL_FILES) $(F77_SRC_FILES) $(C_SRC_FILES) $(H_SRC_FILES) $(F90_SRC_FILES) $(OBJFILES) $(EMBEDDED_FILES)
	@echo Creating $@ ...
	$(LINK) -o $@ $(FFLAGS) $(FOPTIM) $(OBJFILES) $(LIBS)

depend:
	@$(MAKE) -f $(MAKEFILE) links
	$(MAKEDEPEND) -f $(MAKEFILE) -o .for $(DEFINES) $(INCLUDES) $(CPPINCLUDES) $(F77_SRC_FILES)
	$(TOOLSDIR)/f90mkdepend >> $(MAKEFILE)
	-rm -f makedepend.out

lib: libmitgcmuv.a

libmitgcmuv.a: $(OBJFILES)
	ar rcv libmitgcmuv.a $(OBJFILES)
	ar d   libmitgcmuv.a main.o

obj: $(OBJFILES)

links: $(F77_SRC_FILES) $(C_SRC_FILES) $(H_SRC_FILES) $(F90_SRC_FILES) $(SPECIAL_FILES)

small_f: $(F77_PP_SRC_FILES) $(F90_PP_SRC_FILES)

# remove most of the files that "make" generates
clean:
	-rm -rf *.p *.fr9 *.mod  work.{pc,pcl} *.template
	-rm -rf *.o
	-rm -rf *.for *.flowdir
	-rm -rf *.ffr9 $(AD_CLEAN) ad_input*

# remove most of the files that "make" and "make depend" generate
Clean:
	@$(MAKE) -f $(MAKEFILE) clean
	@$(MAKE) -f $(MAKEFILE) cleanlinks
	-rm -f $(SPECIAL_FILES) f90mkdepend.log Makefile.old
	-rm -f taf_command taf_output taf_ad.log taf_ad_flow.log taf_ftl.log

# remove also the executable, files that "genmake2" generates (except Makefile)
#         and output from a run (plus log files from testreport)
CLEAN:
	@$(MAKE) -f $(MAKEFILE) Clean
	-rm -f $(EXECUTABLE) $(EXE_AD) $(EXE_FTL) *.bak
	-rm -f genmake.log genmake_state genmake_*optfile
	-rm -f SIZE.h.mpi genmake.tr_log make.tr_log
	-rm -rf mpi_headers mnc_test_*
	-find $(EXEDIR) -name "*.meta" -exec rm {} \;
	-find $(EXEDIR) -name "*.data" -exec rm {} \;
	-find $(EXEDIR) -name "fort.*" -exec rm {} \;
	-rm -f *.txt STDOUT.* STDERR.* *diagnostics.log *.[0-9][0-9][0-9][0-9].log
	-rm -f datetime costfinal divided.ctrl snapshot* output_adm.txt.diva_*
	-rm -f *_MIT_CE_000.opt0000 costfunction*0000
	-rm -f oad_cp.[0-9][0-9][0-9].?????

makefile:
	$(TOOLSDIR)/genmake2  "-optfile=../build_options/darwin_brewgfortranmpi" "-mods=../code/" "-rootdir=/Users/jklymak/MITgcmc66b/MITgcm"
cleanlinks:
	-find . -type l -exec rm {} \;

# Special targets (SPECIAL_FILES) which are created by make
PACKAGES_CONFIG.h:
	@echo Creating $@ ...
	@$(TOOLSDIR)/convert_cpp_cmd2defines -bPACKAGES_CONFIG_H "Disabled packages:" $(DISABLED_PACKAGES) " " "Enabled packages:" $(ENABLED_PACKAGES) > $@
AD_CONFIG.h:
	@echo Creating $@ ...
	@$(TOOLSDIR)/convert_cpp_cmd2defines "Default version" -bAD_CONFIG_H -UALLOW_ADJOINT_RUN -UALLOW_TANGENTLINEAR_RUN > $@
FC_NAMEMANGLE.h:
	@echo Creating $@ ...
	echo "#define FC_NAMEMANGLE(X)  X ## _" > $@

BUILD_INFO.h:
	@echo Creating $@ ...
	-echo "#define THISVER 'checkpoint66b'" > $@
	-echo "#define THISUSER 'jklymak'" >> $@
	-echo "#define THISDATE 'Wed Jan 11 11:01:34 PST 2017'" >> $@
	-echo "#define THISHOST 'valdez.seos.uvic.ca'" >> $@

# The normal chain of rules is (  .F - .for - .o  )

## This nullifies any default implicit rules concerning these two file types:
## %.o : %.F

# C preprocessing and replacing the _d in constants:
CPPCMD = cat $< |  /usr/local/bin/cpp -traditional -P $(DEFINES) $(INCLUDES) | $(TOOLSDIR)/set64bitConst.sh

.F.for:
	$(CPPCMD)  > $@
.for.o:
	$(FC) $(FFLAGS) $(FOPTIM) -c $<
.F.o:
	$(FC) $(FFLAGS) $(FOPTIM) -c $<
.F90.fr9:
	$(CPPCMD)  > $@
.FF90.ffr9:
	$(CPPCMD)  > $@
.fr9.o:
	$(F90C) $(F90FLAGS) $(F90OPTIM) -c $<
.ffr9.o:
	cp $< $(basename  $<).f90
	$(F90C) $(F90FLAGS) $(F90OPTIM) -c $(F90FIXEDFORMAT) $(basename  $<).f90
.c.o:
	$(CC) $(CFLAGS) $(DEFINES) $(INCLUDES) -c $<
.flow.flowdir:
	$(CPPCMD) > $@

# Special exceptions that use the ( .F - .p - .for - .o ) rule-chain
.F.p:
	$(CPPCMD) > $@
.p.for:
	$(KPP) $(KFLAGS1)$@ $(KFLAGS2) $<


TAMC           = tamc
TAF            = staf

TAF_EXTRA      = 
TAMC_EXTRA     = 
LOCAL_MPI_HEADERS    = 

AD_TAMC_FLAGS        = -reverse -admark ad -i4 -r4 -l tamc_ad.log  -toplevel 'the_main_loop'                -input 'xx_theta_dummy                           xx_salt_dummy                            xx_tr1_dummy                             xx_hflux_dummy                           xx_sflux_dummy                           xx_tauu_dummy                            xx_tauv_dummy                            xx_atemp_dummy                           xx_aqh_dummy                             xx_precip_dummy                          xx_swflux_dummy                          xx_swdown_dummy                          xx_lwflux_dummy                          xx_lwdown_dummy                          xx_evap_dummy                            xx_snowprecip_dummy                      xx_apressure_dummy                       xx_runoff_dummy                          xx_uwind_dummy                           xx_vwind_dummy                           xx_obcsn_dummy                           xx_obcss_dummy                           xx_obcsw_dummy                           xx_obcse_dummy                           xx_sst_dummy                             xx_sss_dummy                             xx_depth_dummy                           xx_diffkr_dummy                          xx_kapgm_dummy                           xx_kapredi_dummy                         xx_bottomdrag_dummy                      xx_efluxy_dummy                          xx_efluxp_dummy                          xx_edtaux_dummy                          xx_edtauy_dummy                          xx_uvel_dummy                            xx_vvel_dummy                            xx_etan_dummy                            xx_gen2d_dummy                           xx_gen3d_dummy                           xx_genarr2d_dummy                        xx_genarr3d_dummy                        xx_gentim2d_dummy                        xx_siarea_dummy                          xx_siheff_dummy                          xx_sihsnow_dummy                         xx_shifwflx_dummy                        xx_relaxsst_dummy                        xx_relaxsss_dummy                        xx_atemp_mean_dummy                      xx_aqh_mean_dummy                        xx_precip_mean_dummy                     xx_swdown_mean_dummy                     xx_uwind_mean_dummy                      xx_vwind_mean_dummy'             -output 'fc'
AD_TAF_FLAGS         = -server fastopt.net -f77 -reverse -i4 -r4 -intrinsic system,flush -l taf_ad.log    -toplevel 'the_main_loop'                -input 'xx_theta_dummy                           xx_salt_dummy                            xx_tr1_dummy                             xx_hflux_dummy                           xx_sflux_dummy                           xx_tauu_dummy                            xx_tauv_dummy                            xx_atemp_dummy                           xx_aqh_dummy                             xx_precip_dummy                          xx_swflux_dummy                          xx_swdown_dummy                          xx_lwflux_dummy                          xx_lwdown_dummy                          xx_evap_dummy                            xx_snowprecip_dummy                      xx_apressure_dummy                       xx_runoff_dummy                          xx_uwind_dummy                           xx_vwind_dummy                           xx_obcsn_dummy                           xx_obcss_dummy                           xx_obcsw_dummy                           xx_obcse_dummy                           xx_sst_dummy                             xx_sss_dummy                             xx_depth_dummy                           xx_diffkr_dummy                          xx_kapgm_dummy                           xx_kapredi_dummy                         xx_bottomdrag_dummy                      xx_efluxy_dummy                          xx_efluxp_dummy                          xx_edtaux_dummy                          xx_edtauy_dummy                          xx_uvel_dummy                            xx_vvel_dummy                            xx_etan_dummy                            xx_gen2d_dummy                           xx_gen3d_dummy                           xx_genarr2d_dummy                        xx_genarr3d_dummy                        xx_gentim2d_dummy                        xx_siarea_dummy                          xx_siheff_dummy                          xx_sihsnow_dummy                         xx_shifwflx_dummy                        xx_relaxsst_dummy                        xx_relaxsss_dummy                        xx_atemp_mean_dummy                      xx_aqh_mean_dummy                        xx_precip_mean_dummy                     xx_swdown_mean_dummy                     xx_uwind_mean_dummy                      xx_vwind_mean_dummy'             -output 'fc'
FTL_TAMC_FLAGS       = -forward -ftlmark g_ -i4 -r4 -l tamc_ftl.log  -toplevel 'the_main_loop'                -input 'xx_theta_dummy                           xx_salt_dummy                            xx_tr1_dummy                             xx_hflux_dummy                           xx_sflux_dummy                           xx_tauu_dummy                            xx_tauv_dummy                            xx_atemp_dummy                           xx_aqh_dummy                             xx_precip_dummy                          xx_swflux_dummy                          xx_swdown_dummy                          xx_lwflux_dummy                          xx_lwdown_dummy                          xx_evap_dummy                            xx_snowprecip_dummy                      xx_apressure_dummy                       xx_runoff_dummy                          xx_uwind_dummy                           xx_vwind_dummy                           xx_obcsn_dummy                           xx_obcss_dummy                           xx_obcsw_dummy                           xx_obcse_dummy                           xx_sst_dummy                             xx_sss_dummy                             xx_depth_dummy                           xx_diffkr_dummy                          xx_kapgm_dummy                           xx_kapredi_dummy                         xx_bottomdrag_dummy                      xx_efluxy_dummy                          xx_efluxp_dummy                          xx_edtaux_dummy                          xx_edtauy_dummy                          xx_uvel_dummy                            xx_vvel_dummy                            xx_etan_dummy                            xx_gen2d_dummy                           xx_gen3d_dummy                           xx_genarr2d_dummy                        xx_genarr3d_dummy                        xx_gentim2d_dummy                        xx_siarea_dummy                          xx_siheff_dummy                          xx_sihsnow_dummy                         xx_shifwflx_dummy                        xx_relaxsst_dummy                        xx_relaxsss_dummy                        xx_atemp_mean_dummy                      xx_aqh_mean_dummy                        xx_precip_mean_dummy                     xx_swdown_mean_dummy                     xx_uwind_mean_dummy                      xx_vwind_mean_dummy'             -output 'fc'
FTL_TAF_FLAGS        = -server fastopt.net -f77 -forward -i4 -r4 -intrinsic system,flush -l taf_ftl.log    -toplevel 'the_main_loop'                -input 'xx_theta_dummy                           xx_salt_dummy                            xx_tr1_dummy                             xx_hflux_dummy                           xx_sflux_dummy                           xx_tauu_dummy                            xx_tauv_dummy                            xx_atemp_dummy                           xx_aqh_dummy                             xx_precip_dummy                          xx_swflux_dummy                          xx_swdown_dummy                          xx_lwflux_dummy                          xx_lwdown_dummy                          xx_evap_dummy                            xx_snowprecip_dummy                      xx_apressure_dummy                       xx_runoff_dummy                          xx_uwind_dummy                           xx_vwind_dummy                           xx_obcsn_dummy                           xx_obcss_dummy                           xx_obcsw_dummy                           xx_obcse_dummy                           xx_sst_dummy                             xx_sss_dummy                             xx_depth_dummy                           xx_diffkr_dummy                          xx_kapgm_dummy                           xx_kapredi_dummy                         xx_bottomdrag_dummy                      xx_efluxy_dummy                          xx_efluxp_dummy                          xx_edtaux_dummy                          xx_edtauy_dummy                          xx_uvel_dummy                            xx_vvel_dummy                            xx_etan_dummy                            xx_gen2d_dummy                           xx_gen3d_dummy                           xx_genarr2d_dummy                        xx_genarr3d_dummy                        xx_gentim2d_dummy                        xx_siarea_dummy                          xx_siheff_dummy                          xx_sihsnow_dummy                         xx_shifwflx_dummy                        xx_relaxsst_dummy                        xx_relaxsss_dummy                        xx_atemp_mean_dummy                      xx_aqh_mean_dummy                        xx_precip_mean_dummy                     xx_swdown_mean_dummy                     xx_uwind_mean_dummy                      xx_vwind_mean_dummy'             -output 'fc'
SVD_TAMC_FLAGS       = -reverse -forward -pure -i4 -r4 -l tamc_svd.log  -toplevel 'the_main_loop'                -input 'xx_theta_dummy                           xx_salt_dummy                            xx_tr1_dummy                             xx_hflux_dummy                           xx_sflux_dummy                           xx_tauu_dummy                            xx_tauv_dummy                            xx_atemp_dummy                           xx_aqh_dummy                             xx_precip_dummy                          xx_swflux_dummy                          xx_swdown_dummy                          xx_lwflux_dummy                          xx_lwdown_dummy                          xx_evap_dummy                            xx_snowprecip_dummy                      xx_apressure_dummy                       xx_runoff_dummy                          xx_uwind_dummy                           xx_vwind_dummy                           xx_obcsn_dummy                           xx_obcss_dummy                           xx_obcsw_dummy                           xx_obcse_dummy                           xx_sst_dummy                             xx_sss_dummy                             xx_depth_dummy                           xx_diffkr_dummy                          xx_kapgm_dummy                           xx_kapredi_dummy                         xx_bottomdrag_dummy                      xx_efluxy_dummy                          xx_efluxp_dummy                          xx_edtaux_dummy                          xx_edtauy_dummy                          xx_uvel_dummy                            xx_vvel_dummy                            xx_etan_dummy                            xx_gen2d_dummy                           xx_gen3d_dummy                           xx_genarr2d_dummy                        xx_genarr3d_dummy                        xx_gentim2d_dummy                        xx_siarea_dummy                          xx_siheff_dummy                          xx_sihsnow_dummy                         xx_shifwflx_dummy                        xx_relaxsst_dummy                        xx_relaxsss_dummy                        xx_atemp_mean_dummy                      xx_aqh_mean_dummy                        xx_precip_mean_dummy                     xx_swdown_mean_dummy                     xx_uwind_mean_dummy                      xx_vwind_mean_dummy'             -output 'fc'
SVD_TAF_FLAGS        = -server fastopt.net -f77 -reverse -forward -pure -i4 -r4 -intrinsic system,flush -l taf_svd.log    -toplevel 'the_main_loop'                -input 'xx_theta_dummy                           xx_salt_dummy                            xx_tr1_dummy                             xx_hflux_dummy                           xx_sflux_dummy                           xx_tauu_dummy                            xx_tauv_dummy                            xx_atemp_dummy                           xx_aqh_dummy                             xx_precip_dummy                          xx_swflux_dummy                          xx_swdown_dummy                          xx_lwflux_dummy                          xx_lwdown_dummy                          xx_evap_dummy                            xx_snowprecip_dummy                      xx_apressure_dummy                       xx_runoff_dummy                          xx_uwind_dummy                           xx_vwind_dummy                           xx_obcsn_dummy                           xx_obcss_dummy                           xx_obcsw_dummy                           xx_obcse_dummy                           xx_sst_dummy                             xx_sss_dummy                             xx_depth_dummy                           xx_diffkr_dummy                          xx_kapgm_dummy                           xx_kapredi_dummy                         xx_bottomdrag_dummy                      xx_efluxy_dummy                          xx_efluxp_dummy                          xx_edtaux_dummy                          xx_edtauy_dummy                          xx_uvel_dummy                            xx_vvel_dummy                            xx_etan_dummy                            xx_gen2d_dummy                           xx_gen3d_dummy                           xx_genarr2d_dummy                        xx_genarr3d_dummy                        xx_gentim2d_dummy                        xx_siarea_dummy                          xx_siheff_dummy                          xx_sihsnow_dummy                         xx_shifwflx_dummy                        xx_relaxsst_dummy                        xx_relaxsss_dummy                        xx_atemp_mean_dummy                      xx_aqh_mean_dummy                        xx_precip_mean_dummy                     xx_swdown_mean_dummy                     xx_uwind_mean_dummy                      xx_vwind_mean_dummy'             -output 'fc'

AD_FILES =  \
 diagnostics_is_on.for \
 gad_advection.for \
 gad_biharm_r.for \
 gad_biharm_x.for \
 gad_biharm_y.for \
 gad_c2_adv_r.for \
 gad_c2_impl_r.for \
 gad_c2_adv_x.for \
 gad_c2_adv_y.for \
 gad_c4_adv_r.for \
 gad_c4_adv_x.for \
 gad_c4_adv_y.for \
 gad_calc_rhs.for \
 gad_del2.for \
 gad_diff_r.for \
 gad_diff_x.for \
 gad_diff_y.for \
 gad_dst2u1_adv_r.for \
 gad_dst2u1_impl_r.for \
 gad_dst2u1_adv_x.for \
 gad_dst2u1_adv_y.for \
 gad_dst3_adv_x.for \
 gad_dst3_adv_y.for \
 gad_dst3_adv_r.for \
 gad_dst3fl_adv_x.for \
 gad_dst3fl_adv_y.for \
 gad_dst3fl_adv_r.for \
 gad_dst3fl_impl_r.for \
 gad_fluxlimit_adv_r.for \
 gad_fluxlimit_impl_r.for \
 gad_fluxlimit_adv_x.for \
 gad_fluxlimit_adv_y.for \
 gad_grad_x.for \
 gad_grad_y.for \
 gad_implicit_r.for \
 gad_init_varia.for \
 gad_os7mp_adv_x.for \
 gad_os7mp_adv_y.for \
 gad_os7mp_adv_r.for \
 gad_read_pickup.for \
 gad_u3_adv_r.for \
 gad_u3c4_impl_r.for \
 gad_u3_adv_x.for \
 gad_u3_adv_y.for \
 gad_som_advect.for \
 gad_som_adv_r.for \
 gad_som_adv_x.for \
 gad_som_adv_y.for \
 gad_som_fill_cs_corner.for \
 gad_som_lim_r.for \
 gad_som_prep_cs_corner.for \
 gad_som_exchanges.for \
 gad_exch_som.for \
 mom_calc_absvort3.for \
 mom_calc_hdiv.for \
 mom_calc_hfacz.for \
 mom_calc_ke.for \
 mom_calc_relvort3.for \
 mom_calc_strain.for \
 mom_calc_tension.for \
 mom_calc_visc.for \
 mom_hdissip.for \
 mom_quasihydrostatic.for \
 mom_u_coriolis_nh.for \
 mom_u_metric_nh.for \
 mom_u_bottomdrag.for \
 mom_u_rviscflux.for \
 mom_u_sidedrag.for \
 mom_v_coriolis_nh.for \
 mom_v_metric_nh.for \
 mom_v_bottomdrag.for \
 mom_v_rviscflux.for \
 mom_v_sidedrag.for \
 mom_calc_rtrans.for \
 mom_fluxform.for \
 mom_u_adv_uu.for \
 mom_u_adv_vu.for \
 mom_u_adv_wu.for \
 mom_u_coriolis.for \
 mom_u_del2u.for \
 mom_u_metric_cylinder.for \
 mom_u_metric_sphere.for \
 mom_u_xviscflux.for \
 mom_u_yviscflux.for \
 mom_v_adv_uv.for \
 mom_v_adv_vv.for \
 mom_v_adv_wv.for \
 mom_v_coriolis.for \
 mom_v_del2v.for \
 mom_v_metric_cylinder.for \
 mom_v_metric_sphere.for \
 mom_v_xviscflux.for \
 mom_v_yviscflux.for \
 mom_vecinv.for \
 mom_vi_coriolis.for \
 mom_vi_del2uv.for \
 mom_vi_hdissip.for \
 mom_vi_u_coriolis.for \
 mom_vi_u_coriolis_c4.for \
 mom_vi_u_grad_ke.for \
 mom_vi_u_vertshear.for \
 mom_vi_v_coriolis.for \
 mom_vi_v_coriolis_c4.for \
 mom_vi_v_grad_ke.for \
 mom_vi_v_vertshear.for \
 obcs_adjust_uvice.for \
 obcs_apply_eta.for \
 obcs_apply_seaice.for \
 obcs_apply_uvice.for \
 obcs_apply_r_star.for \
 obcs_apply_surf_dr.for \
 obcs_apply_ts.for \
 obcs_apply_uv.for \
 obcs_apply_w.for \
 obcs_apply_ptracer.for \
 obcs_calc.for \
 obcs_calc_stevens.for \
 obcs_copy_uv_n.for \
 obcs_save_uv_n.for \
 obcs_copy_tracer.for \
 obcs_u1_adv_tracer.for \
 obcs_exchanges.for \
 obcs_exf_load.for \
 obcs_fields_load.for \
 obcs_init_variables.for \
 obcs_prescribe_read.for \
 obcs_read_pickup.for \
 obcs_sponge.for \
 obcs_balance_flow.for \
 orlanski_east.for \
 orlanski_north.for \
 orlanski_south.for \
 orlanski_west.for \
 orlanski_init.for \
 read_fld_xyz_rs.for \
 read_fld_xyz_rl.for \
 read_fld_xy_rs.for \
 read_fld_xy_rl.for \
 read_rec.for \
 timeave_cumul_1k1t.for \
 timeave_cumul_1t.for \
 timeave_cumul_1vfc.for \
 timeave_cumul_2v.for \
 timeave_cumul_2vfc.for \
 timeave_cumulate.for \
 timeave_cumul_dif_1t.for \
 timeave_norma_2v.for \
 timeave_normalize.for \
 timeave_reset.for \
 timeave_statvars.for \
 timeave_statv_write.for \
 timeave_surf_flux.for \
 different_multiple.for \
 fill_cs_corner_ag_rl.for \
 fill_cs_corner_tr_rl.for \
 fill_cs_corner_uv_rs.for \
 fill_cs_corner_uv_rl.for \
 get_periodic_interval.for \
 lef_zero.for \
 exch_sm_3d_rl.for \
 exch_3d_rs.for \
 exch_3d_rl.for \
 exch_xy_rl.for \
 exch_xy_rs.for \
 exch_xyz_rl.for \
 exch_xyz_rs.for \
 exch_uv_3d_rs.for \
 exch_uv_3d_rl.for \
 exch_uv_xy_rs.for \
 exch_uv_xy_rl.for \
 exch_uv_xyz_rs.for \
 exch_uv_xyz_rl.for \
 exch_uv_agrid_3d_rs.for \
 exch_uv_agrid_3d_rl.for \
 exch_uv_dgrid_3d_rs.for \
 exch_uv_dgrid_3d_rl.for \
 adams_bashforth2.for \
 adams_bashforth3.for \
 add_walls2masks.for \
 apply_forcing.for \
 calc_3d_diffusivity.for \
 calc_adv_flow.for \
 calc_div_ghat.for \
 calc_grad_phi_fv.for \
 calc_grad_phi_hyd.for \
 calc_grad_phi_surf.for \
 calc_ivdc.for \
 calc_phi_hyd.for \
 calc_r_star.for \
 calc_surf_dr.for \
 calc_viscosity.for \
 calc_wsurf_tr.for \
 cg2d_nsa.for \
 convective_adjustment.for \
 convective_adjustment_ini.for \
 convective_weights.for \
 convectively_mixtracer.for \
 correction_step.for \
 cycle_ab_tracer.for \
 cycle_tracer.for \
 diags_phi_hyd.for \
 diags_phi_rlow.for \
 diags_rho.for \
 do_atmospheric_phys.for \
 do_fields_blocking_exchanges.for \
 do_oceanic_phys.for \
 do_stagger_fields_exchanges.for \
 dynamics.for \
 external_fields_load.for \
 external_forcing_surf.for \
 forcing_surf_relax.for \
 find_alpha.for \
 find_rho.for \
 forward_step.for \
 freesurf_rescale_g.for \
 freeze_surface.for \
 grad_sigma.for \
 impldiff.for \
 ini_cartesian_grid.for \
 ini_cg2d.for \
 ini_cori.for \
 ini_curvilinear_grid.for \
 ini_cylinder_grid.for \
 ini_depths.for \
 ini_ffields.for \
 ini_fields.for \
 ini_forcing.for \
 ini_grid.for \
 ini_linear_phisurf.for \
 ini_masks_etc.for \
 ini_mixing.for \
 ini_nh_fields.for \
 ini_nlfs_vars.for \
 ini_p_ground.for \
 ini_pressure.for \
 ini_psurf.for \
 ini_salt.for \
 ini_sigma_hfac.for \
 ini_spherical_polar_grid.for \
 ini_theta.for \
 ini_dynvars.for \
 ini_vel.for \
 ini_vertical_grid.for \
 initialise_varia.for \
 integrate_for_w.for \
 integr_continuity.for \
 load_fields_driver.for \
 load_grid_spacing.for \
 main_do_loop.for \
 momentum_correction_step.for \
 packages_init_variables.for \
 pressure_for_eos.for \
 read_pickup.for \
 remove_mean.for \
 reset_nlfs_vars.for \
 rotate_uv2en.for \
 salt_integrate.for \
 temp_integrate.for \
 seawater.for \
 solve_for_pressure.for \
 state_summary.for \
 solve_pentadiagonal.for \
 solve_tridiagonal.for \
 taueddy_init_varia.for \
 taueddy_tendency_apply.for \
 timestep.for \
 the_main_loop.for \
 thermodynamics.for \
 timestep_tracer.for \
 tracers_correction_step.for \
 update_cg2d.for \
 update_etah.for \
 update_etaws.for \
 update_masks_etc.for \
 update_r_star.for \
 update_sigma.for \
 update_surf_dr.for \
 swfrac.for

# ... AD ...
adall: ad_exe_target
adtaf: ad_taf_output.for
adtamc: ad_tamc_output.for

ad_exe_target:
	@echo Update AD_CONFIG.h and make $(EXE_AD)
	@$(TOOLSDIR)/convert_cpp_cmd2defines "Adjoint version" -bAD_CONFIG_H -DALLOW_ADJOINT_RUN -UALLOW_TANGENTLINEAR_RUN > ad_config.template
	@cmp ad_config.template AD_CONFIG.h || cat ad_config.template > AD_CONFIG.h
	@-rm -f ad_config.template
	$(MAKE) -f $(MAKEFILE) $(EXE_AD)

ad_input_code.for: $(AD_FILES) $(AD_FLOW_FILES)
	@$(TOOLSDIR)/convert_cpp_cmd2defines "Adjoint version" -bAD_CONFIG_H -DALLOW_ADJOINT_RUN -UALLOW_TANGENTLINEAR_RUN > ad_config.template
	cmp ad_config.template AD_CONFIG.h || cat ad_config.template > AD_CONFIG.h
	@-rm -f ad_config.template
	@$(MAKE) -f $(MAKEFILE) $(F77_PP_SRC_FILES)
	@$(MAKE) -f $(MAKEFILE) $(FLOWFILES)
	cat $(FLOWFILES) $(AD_FILES) | sed -f $(TOOLSDIR)/remove_comments_sed > ad_input_code.for

adtafonly:
	$(TAF) $(AD_TAF_FLAGS) $(TAF_EXTRA) ad_input_code.for
	ls -l ad_input_code_ad.for
	cat ad_input_code_ad.for | sed -f $(TOOLSDIR)/adjoint_sed > ad_taf_output.for

# ... send 1 file to TAF ...
ad_taf_output.for: ad_input_code.for
	@-rm -f ad_input_code_ad.for ; echo ''
	$(TAF) $(AD_TAF_FLAGS) $(TAF_EXTRA) ad_input_code.for
	ls -l ad_input_code_ad.for
	cat ad_input_code_ad.for | sed -f $(TOOLSDIR)/adjoint_sed > ad_taf_output.for

$(EXE_AD): $(SPECIAL_FILES) $(H_SRC_FILES) ad_taf_output.o $(NON_AD_F77_SRC_FILES:.F=.o) $(F90_SRC_FILES:.F90=.o) $(C_SRC_FILES:.c=.o) $(EMBEDDED_FILES)
	$(LINK) -o ${EXE_AD} $(FFLAGS) $(FOPTIM) ad_taf_output.o $(NON_AD_F77_SRC_FILES:.F=.o) $(F90_SRC_FILES:.F90=.o) $(C_SRC_FILES:.c=.o) $(LIBS)

adobj: ad_taf_output.o $(NON_AD_F77_SRC_FILES:.F=.o) $(F90_SRC_FILES:.F90=.o) $(C_SRC_FILES:.c=.o)

adonlyfwd:
	patch < $(TOOLSDIR)/ad_taf_output.f.onlyfwd.diff

adtrick:
	patch < $(TOOLSDIR)/ad_taf_output.f.adtrick.diff

ad_tamc_output.for: ad_input_code.for
	$(TAMC) $(AD_TAMC_FLAGS) $(TAMC_EXTRA) ad_input_code.for
	cat ad_input_code_ad.for | sed -f $(TOOLSDIR)/adjoint_sed > ad_tamc_output.for

ad_tamc: ad_tamc_output.o $(OBJFILES)
	$(LINK) -o mitgcmuv_ad $(FFLAGS) $(FOPTIM) $(OBJFILES) ad_tamc_output.o $(LIBS)

# ... FTL ...
ftlall: ftl_exe_target
ftltaf: ftl_taf_output.for
ftltamc: ftl_tamc_output.for

ftl_exe_target:
	@echo Update AD_CONFIG.h and make $(EXE_FTL)
	@$(TOOLSDIR)/convert_cpp_cmd2defines "TangLin version" -bAD_CONFIG_H -UALLOW_ADJOINT_RUN -DALLOW_TANGENTLINEAR_RUN > ad_config.template
	@cmp ad_config.template AD_CONFIG.h || cat ad_config.template > AD_CONFIG.h
	@-rm -f ad_config.template
	$(MAKE) -f $(MAKEFILE) $(EXE_FTL)

ftl_input_code.for: $(AD_FILES)
	@$(TOOLSDIR)/convert_cpp_cmd2defines "TangLin version" -bAD_CONFIG_H -UALLOW_ADJOINT_RUN -DALLOW_TANGENTLINEAR_RUN > ad_config.template
	cmp ad_config.template AD_CONFIG.h || cat ad_config.template > AD_CONFIG.h
	@-rm -f ad_config.template
	@$(MAKE) -f $(MAKEFILE) $(F77_PP_SRC_FILES)
	@$(MAKE) -f $(MAKEFILE) $(AD_FLOW_FILES)
	cat $(AD_FLOW_FILES) $(AD_FILES) | sed -f $(TOOLSDIR)/remove_comments_sed > ftl_input_code.for

ftltafonly:
	$(TAF) $(FTL_TAF_FLAGS) $(TAF_EXTRA) ftl_input_code.for
	ls -l ftl_input_code_tl.for
	cat ftl_input_code_tl.for | sed -f $(TOOLSDIR)/adjoint_sed > ftl_taf_output.for

# ... send 1 file to TAF ...
ftl_taf_output.for: ftl_input_code.for
	@-rm -f ftl_input_code_tl.for ; echo ''
	$(TAF) $(FTL_TAF_FLAGS) $(TAF_EXTRA) ftl_input_code.for
	ls -l ftl_input_code_tl.for
	cat ftl_input_code_tl.for | sed -f $(TOOLSDIR)/adjoint_sed > ftl_taf_output.for

$(EXE_FTL): $(SPECIAL_FILES) $(H_SRC_FILES) ftl_taf_output.o $(NON_AD_F77_SRC_FILES:.F=.o) $(F90_SRC_FILES:.F90=.o) $(C_SRC_FILES:.c=.o) $(EMBEDDED_FILES)
	$(LINK) -o ${EXE_FTL} $(FFLAGS) $(FOPTIM) ftl_taf_output.o $(NON_AD_F77_SRC_FILES:.F=.o) $(F90_SRC_FILES:.F90=.o) $(C_SRC_FILES:.c=.o) $(LIBS)

ftl_tamc_output.for: ftl_input_code.for
	$(TAMC) $(FTL_TAMC_FLAGS) $(TAMC_EXTRA) ftl_input_code.for
	cat ftl_input_code_ftl.for | sed -f $(TOOLSDIR)/adjoint_sed > ftl_tamc_output.for

ftl_tamc: ftl_tamc_output.o $(OBJFILES)
	$(LINK) -o mitgcmuv_ftl $(FFLAGS) $(FOPTIM) $(OBJFILES) ftl_tamc_output.o $(LIBS)

# ... SVD ...
svdtaf: ad_taf_output.for ftl_taf_output.for
	@echo "--->>> Only ran TAF to generate SVD code!    <<<---"
	@echo "--->>> Do make svdall afterwards to compile. <<<---"
svdall: svd_touch svd_taf

svd_taf: $(OBJFILES)
	$(LINK) -o mitgcmuv_svd $(FFLAGS) $(FOPTIM) $(OBJFILES) ad_taf_output.o ftl_taf_output.o $(LIBS)

	@echo "--->>> Only COMPILE svd code! <<<---"
	@echo "--->>> Assumes you previously <<<---"
	@echo "--->>> did make svdtaf        <<<---"

svd_touch:
	@echo "--->>> Only COMPILE svd code! <<<---"
	@echo "--->>> Assumes you previously <<<---"
	@echo "--->>> did make svdtaf        <<<---"
	touch ad_taf_output.for ftl_taf_output.for
	$(FC) $(FFLAGS) $(FOPTIM) -c ad_taf_output.for
	$(FC) $(FFLAGS) $(FOPTIM) -c ftl_taf_output.for
	@$(TOOLSDIR)/convert_cpp_cmd2defines "SVD version" -bAD_CONFIG_H -UALLOW_ADJOINT_RUN -DALLOW_TANGENTLINEAR_RUN > ad_config.template
	cmp ad_config.template AD_CONFIG.h || cat ad_config.template > AD_CONFIG.h
	@-rm -f ad_config.template

# This section creates symbolic links


#  These files are linked from ../code/
 CPP_OPTIONS.h SIZE.h :
	if [ ! -L $@ ]; then $(LN) ../code//$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/pkg/debug
 DEBUG_OPTIONS.h chksum_tiled.F debug_call.F debug_cs_corner_uv.F debug_enter.F debug_fld_stats_rl.F debug_fld_stats_rs.F debug_leave.F debug_msg.F debug_stats_rl.F debug_stats_rs.F fill_in_corners_rl.F write_fullarray_rl.F write_fullarray_rs.F debug_ad.flow :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/pkg/debug/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/pkg/diagnostics
 DIAGNOSTICS.h DIAGNOSTICS_CALC.h DIAGNOSTICS_SIZE.h DIAGSTATS_REGIONS.h DIAG_OPTIONS.h diag_calc_psivel.F diag_cg2d.F diag_vegtile_fill.F diagnostics_addtolist.F diagnostics_calc_phivel.F diagnostics_check.F diagnostics_clear.F diagnostics_fill.F diagnostics_fill_field.F diagnostics_fill_rs.F diagnostics_fill_state.F diagnostics_fract_fill.F diagnostics_init_early.F diagnostics_init_fixed.F diagnostics_init_varia.F diagnostics_interp_p2p.F diagnostics_interp_vert.F diagnostics_is_on.F diagnostics_list_check.F diagnostics_main_init.F diagnostics_mnc_out.F diagnostics_out.F diagnostics_read_pickup.F diagnostics_readparms.F diagnostics_scale_fill.F diagnostics_scale_fill_rs.F diagnostics_set_calc.F diagnostics_set_levels.F diagnostics_set_pointers.F diagnostics_setdiag.F diagnostics_status_error.F diagnostics_sum_levels.F diagnostics_summary.F diagnostics_switch_onoff.F diagnostics_utils.F diagnostics_write.F diagnostics_write_pickup.F diagstats_ascii_out.F diagstats_calc.F diagstats_clear.F diagstats_close_io.F diagstats_fill.F diagstats_global.F diagstats_ini_io.F diagstats_local.F diagstats_mnc_out.F diagstats_others_calc.F diagstats_output.F diagstats_set_pointers.F diagstats_set_regions.F diagstats_setdiag.F diagnostics_ad.flow :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/pkg/diagnostics/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/pkg/generic_advdiff
 GAD.h GAD_FLUX_LIMITER.h GAD_OPTIONS.h GAD_SOM_VARS.h gad_ad_check_lev1_dir.h gad_ad_check_lev2_dir.h gad_ad_check_lev3_dir.h gad_ad_check_lev4_dir.h gad_advection.F gad_advscheme.F gad_biharm_r.F gad_biharm_x.F gad_biharm_y.F gad_c2_adv_r.F gad_c2_adv_x.F gad_c2_adv_y.F gad_c2_impl_r.F gad_c4_adv_r.F gad_c4_adv_x.F gad_c4_adv_y.F gad_calc_rhs.F gad_check.F gad_del2.F gad_diagnostics_init.F gad_diagnostics_state.F gad_diff_r.F gad_diff_x.F gad_diff_y.F gad_dst2u1_adv_r.F gad_dst2u1_adv_x.F gad_dst2u1_adv_y.F gad_dst2u1_impl_r.F gad_dst3_adv_r.F gad_dst3_adv_x.F gad_dst3_adv_y.F gad_dst3fl_adv_r.F gad_dst3fl_adv_x.F gad_dst3fl_adv_y.F gad_dst3fl_impl_r.F gad_exch_som.F gad_fluxlimit_adv_r.F gad_fluxlimit_adv_x.F gad_fluxlimit_adv_y.F gad_fluxlimit_impl_r.F gad_grad_x.F gad_grad_y.F gad_implicit_r.F gad_init_fixed.F gad_init_varia.F gad_os7mp_adv_r.F gad_os7mp_adv_x.F gad_os7mp_adv_y.F gad_osc_hat_r.F gad_osc_hat_x.F gad_osc_hat_y.F gad_osc_mul_r.F gad_osc_mul_x.F gad_osc_mul_y.F gad_plm_fun.F gad_ppm_adv_r.F gad_ppm_adv_x.F gad_ppm_adv_y.F gad_ppm_flx_r.F gad_ppm_flx_x.F gad_ppm_flx_y.F gad_ppm_fun.F gad_ppm_hat_r.F gad_ppm_hat_x.F gad_ppm_hat_y.F gad_ppm_p3e_r.F gad_ppm_p3e_x.F gad_ppm_p3e_y.F gad_pqm_adv_r.F gad_pqm_adv_x.F gad_pqm_adv_y.F gad_pqm_flx_r.F gad_pqm_flx_x.F gad_pqm_flx_y.F gad_pqm_fun.F gad_pqm_hat_r.F gad_pqm_hat_x.F gad_pqm_hat_y.F gad_pqm_p5e_r.F gad_pqm_p5e_x.F gad_pqm_p5e_y.F gad_read_pickup.F gad_som_adv_r.F gad_som_adv_x.F gad_som_adv_y.F gad_som_advect.F gad_som_exchanges.F gad_som_fill_cs_corner.F gad_som_lim_r.F gad_som_prep_cs_corner.F gad_u3_adv_r.F gad_u3_adv_x.F gad_u3_adv_y.F gad_u3c4_impl_r.F gad_write_pickup.F salt_fill.F :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/pkg/generic_advdiff/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/pkg/kl10
 KL10.h KL10_DIAGS.h KL10_OPTIONS.h KL10_TAVE.h kl10_calc.F kl10_calc_diff.F kl10_calc_visc.F kl10_check.F kl10_diagnostics_init.F kl10_init_fixed.F kl10_init_varia.F kl10_output.F kl10_readparms.F :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/pkg/kl10/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/pkg/mdsio
 MDSIO_BUFF_3D.h MDSIO_BUFF_WH.h MDSIO_OPTIONS.h mdsio_buffertorl.F mdsio_buffertors.F mdsio_check4file.F mdsio_facef_read.F mdsio_gl.F mdsio_gl_slice.F mdsio_pass_r4torl.F mdsio_pass_r4tors.F mdsio_pass_r8torl.F mdsio_pass_r8tors.F mdsio_rd_rec_rl.F mdsio_rd_rec_rs.F mdsio_read_field.F mdsio_read_meta.F mdsio_read_section.F mdsio_read_tape.F mdsio_read_whalos.F mdsio_readvec_loc.F mdsio_rw_field.F mdsio_rw_slice.F mdsio_seg4torl.F mdsio_seg4tors.F mdsio_seg8torl.F mdsio_seg8tors.F mdsio_segxtorx_2d.F mdsio_wr_metafiles.F mdsio_wr_rec_rl.F mdsio_wr_rec_rs.F mdsio_write_field.F mdsio_write_meta.F mdsio_write_section.F mdsio_write_tape.F mdsio_write_whalos.F mdsio_writelocal.F mdsio_writevec_loc.F mdsio_ad.flow :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/pkg/mdsio/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/pkg/mom_common
 MOM_COMMON_OPTIONS.h MOM_VISC.h mom_calc_3d_strain.F mom_calc_absvort3.F mom_calc_hdiv.F mom_calc_hfacz.F mom_calc_ke.F mom_calc_relvort3.F mom_calc_smag_3d.F mom_calc_strain.F mom_calc_tension.F mom_calc_visc.F mom_diagnostics_init.F mom_hdissip.F mom_init_fixed.F mom_quasihydrostatic.F mom_u_botdrag_impl.F mom_u_bottomdrag.F mom_u_coriolis_nh.F mom_u_implicit_r.F mom_u_metric_nh.F mom_u_rviscflux.F mom_u_sidedrag.F mom_uv_smag_3d.F mom_v_botdrag_impl.F mom_v_bottomdrag.F mom_v_coriolis_nh.F mom_v_implicit_r.F mom_v_metric_nh.F mom_v_rviscflux.F mom_v_sidedrag.F mom_w_coriolis_nh.F mom_w_metric_nh.F mom_w_sidedrag.F mom_w_smag_3d.F :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/pkg/mom_common/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/pkg/mom_fluxform
 MOM_FLUXFORM.h MOM_FLUXFORM_OPTIONS.h mom_calc_rtrans.F mom_fluxform.F mom_u_adv_uu.F mom_u_adv_vu.F mom_u_adv_wu.F mom_u_coriolis.F mom_u_del2u.F mom_u_metric_cylinder.F mom_u_metric_sphere.F mom_u_xviscflux.F mom_u_yviscflux.F mom_uv_boundary.F mom_v_adv_uv.F mom_v_adv_vv.F mom_v_adv_wv.F mom_v_coriolis.F mom_v_del2v.F mom_v_metric_cylinder.F mom_v_metric_sphere.F mom_v_xviscflux.F mom_v_yviscflux.F :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/pkg/mom_fluxform/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/pkg/mom_vecinv
 MOM_VECINV_OPTIONS.h mom_vecinv.F mom_vi_coriolis.F mom_vi_del2uv.F mom_vi_hdissip.F mom_vi_u_coriolis.F mom_vi_u_coriolis_c4.F mom_vi_u_grad_ke.F mom_vi_u_vertshear.F mom_vi_v_coriolis.F mom_vi_v_coriolis_c4.F mom_vi_v_grad_ke.F mom_vi_v_vertshear.F :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/pkg/mom_vecinv/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/pkg/monitor
 MONITOR.h MONITOR_OPTIONS.h mon_advcfl.F mon_advcflw.F mon_advcflw2.F mon_calc_advcfl.F mon_calc_stats_rl.F mon_calc_stats_rs.F mon_init.F mon_ke.F mon_out.F mon_printstats_rl.F mon_printstats_rs.F mon_set_iounit.F mon_set_pref.F mon_solution.F mon_stats_latbnd_rl.F mon_stats_rl.F mon_stats_rs.F mon_surfcor.F mon_vort3.F mon_writestats_rl.F mon_writestats_rs.F monitor.F monitor_ad.F monitor_g.F monitor_ad.flow :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/pkg/monitor/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/pkg/obcs
 OBCS_FIELDS.h OBCS_GRID.h OBCS_OPTIONS.h OBCS_PARAMS.h OBCS_PTRACERS.h OBCS_SEAICE.h ORLANSKI.h obcs_ad_check_lev1_dir.h obcs_ad_check_lev2_dir.h obcs_ad_check_lev3_dir.h obcs_ad_check_lev4_dir.h obcs_add_tides.F obcs_adjust_uvice.F obcs_apply_eta.F obcs_apply_ptracer.F obcs_apply_r_star.F obcs_apply_seaice.F obcs_apply_surf_dr.F obcs_apply_ts.F obcs_apply_uv.F obcs_apply_uvice.F obcs_apply_w.F obcs_balance_flow.F obcs_calc.F obcs_calc_stevens.F obcs_check.F obcs_check_depths.F obcs_copy_tracer.F obcs_copy_uv_n.F obcs_diag_balance.F obcs_exchanges.F obcs_exf_load.F obcs_fields_load.F obcs_init_fixed.F obcs_init_variables.F obcs_mon_stats.F obcs_monitor.F obcs_output.F obcs_prescribe_read.F obcs_read_pickup.F obcs_readparms.F obcs_save_uv_n.F obcs_seaice_sponge.F obcs_set_connect.F obcs_sponge.F obcs_u1_adv_tracer.F obcs_write_pickup.F orlanski_east.F orlanski_init.F orlanski_north.F orlanski_south.F orlanski_west.F obcs_ad.flow :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/pkg/obcs/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/pkg/rw
 RW_MFLDS.h RW_OPTIONS.h get_write_global_fld.F read_fld_xy_rl.F read_fld_xy_rs.F read_fld_xyz_rl.F read_fld_xyz_rs.F read_glvec_rl.F read_glvec_rs.F read_mflds.F read_rec.F set_write_global_fld.F write_fld_3d_rl.F write_fld_3d_rs.F write_fld_s3d_rl.F write_fld_s3d_rs.F write_fld_xy_rl.F write_fld_xy_rs.F write_fld_xyz_rl.F write_fld_xyz_rs.F write_glvec_rl.F write_glvec_rs.F write_local_rl.F write_local_rs.F write_rec.F rw_ad.flow :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/pkg/rw/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/pkg/timeave
 TIMEAVE_OPTIONS.h TIMEAVE_STATV.h timeave_cumul_1k1t.F timeave_cumul_1t.F timeave_cumul_1vfc.F timeave_cumul_2v.F timeave_cumul_2vfc.F timeave_cumul_dif_1t.F timeave_cumulate.F timeave_init_fixed.F timeave_norma_2v.F timeave_normalize.F timeave_reset.F timeave_statv_write.F timeave_statvars.F timeave_surf_flux.F :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/pkg/timeave/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/eesupp/src
 all_proc_die.F bar2.F bar_check.F barrier.F check_threads.F comm_stats.F cumulsum_z_tile.F diff_phase_multiple.F different_multiple.F eeboot.F eeboot_minimal.F eedata_example.F eedie.F eeintro_msg.F eeset_parms.F eewrite_eeenv.F exch0_r4.F exch0_r8.F exch0_rl.F exch0_rs.F exch1_bg_r4_cube.F exch1_bg_r8_cube.F exch1_bg_rl_cube.F exch1_bg_rs_cube.F exch1_r4.F exch1_r4_cube.F exch1_r8.F exch1_r8_cube.F exch1_rl.F exch1_rl_ad.F exch1_rl_cube.F exch1_rl_cube_ad.F exch1_rs.F exch1_rs_ad.F exch1_rs_cube.F exch1_rs_cube_ad.F exch1_uv_r4_cube.F exch1_uv_r8_cube.F exch1_uv_rl_cube.F exch1_uv_rs_cube.F exch1_z_r4_cube.F exch1_z_r8_cube.F exch1_z_rl_cube.F exch1_z_rs_cube.F exch_3d_r4.F exch_3d_r8.F exch_3d_rl.F exch_3d_rs.F exch_cycle_ebl.F exch_init.F exch_r4_recv_get_x.F exch_r4_recv_get_y.F exch_r4_send_put_x.F exch_r4_send_put_y.F exch_r8_recv_get_x.F exch_r8_recv_get_y.F exch_r8_send_put_x.F exch_r8_send_put_y.F exch_rl_recv_get_x.F exch_rl_recv_get_y.F exch_rl_send_put_x.F exch_rl_send_put_y.F exch_rs_recv_get_x.F exch_rs_recv_get_y.F exch_rs_send_put_x.F exch_rs_send_put_y.F exch_s3d_r4.F exch_s3d_r8.F exch_s3d_rl.F exch_s3d_rs.F exch_sm_3d_r4.F exch_sm_3d_r8.F exch_sm_3d_rl.F exch_sm_3d_rs.F exch_uv_3d_r4.F exch_uv_3d_r8.F exch_uv_3d_rl.F exch_uv_3d_rs.F exch_uv_agrid_3d_r4.F exch_uv_agrid_3d_r8.F exch_uv_agrid_3d_rl.F exch_uv_agrid_3d_rs.F exch_uv_bgrid_3d_r4.F exch_uv_bgrid_3d_r8.F exch_uv_bgrid_3d_rl.F exch_uv_bgrid_3d_rs.F exch_uv_dgrid_3d_r4.F exch_uv_dgrid_3d_r8.F exch_uv_dgrid_3d_rl.F exch_uv_dgrid_3d_rs.F exch_uv_xy_r4.F exch_uv_xy_r8.F exch_uv_xy_rl.F exch_uv_xy_rs.F exch_uv_xyz_r4.F exch_uv_xyz_r8.F exch_uv_xyz_rl.F exch_uv_xyz_rs.F exch_xy_r4.F exch_xy_r8.F exch_xy_rl.F exch_xy_rs.F exch_xyz_r4.F exch_xyz_r8.F exch_xyz_rl.F exch_xyz_rs.F exch_z_3d_r4.F exch_z_3d_r8.F exch_z_3d_rl.F exch_z_3d_rs.F fill_cs_corner_ag_rl.F fill_cs_corner_tr_rl.F fill_cs_corner_uv_rl.F fill_cs_corner_uv_rs.F fool_the_compiler.F gather_2d_r4.F gather_2d_r8.F gather_2d_wh_r4.F gather_2d_wh_r8.F gather_vec_r4.F gather_vec_r8.F gather_xz.F gather_yz.F get_periodic_interval.F global_max.F global_sum.F global_sum_singlecpu.F global_sum_tile.F global_vec_sum.F gsl_ieee_env.c gsum.F ini_communication_patterns.F ini_procs.F ini_threading_environment.F lef_zero.F main.F master_cpu_io.F master_cpu_thread.F mds_byteswapi4.F mds_byteswapr4.F mds_byteswapr8.F mds_flush.F mds_reclen.F mdsfindunit.F memsync.F nml_change_syntax.F nml_set_terminator.F open_copy_data_file.F print.F ptwrapper.c reset_halo.F scatter_2d_r4.F scatter_2d_r8.F scatter_2d_wh_r4.F scatter_2d_wh_r8.F scatter_vec_r4.F scatter_vec_r8.F scatter_xz.F scatter_yz.F setdir.c setrlstk.c sigreg.c stop_if_error.F tim.c timer_stats.c timers.F utils.F write_utils.F eesupp.flow exch1_ad.flow :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/eesupp/src/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/model/src
 adams_bashforth2.F adams_bashforth3.F add_walls2masks.F apply_forcing.F calc_3d_diffusivity.F calc_adv_flow.F calc_div_ghat.F calc_eddy_stress.F calc_grad_phi_fv.F calc_grad_phi_hyd.F calc_grad_phi_surf.F calc_grid_angles.F calc_gw.F calc_ivdc.F calc_oce_mxlayer.F calc_phi_hyd.F calc_r_star.F calc_surf_dr.F calc_viscosity.F calc_wsurf_tr.F cg2d.F cg2d_ex0.F cg2d_nsa.F cg2d_sr.F cg3d.F cg3d_ex0.F check_pickup.F config_check.F config_summary.F convective_adjustment.F convective_adjustment_ini.F convective_weights.F convectively_mixtracer.F correction_step.F cycle_ab_tracer.F cycle_tracer.F diags_oceanic_surf_flux.F diags_phi_hyd.F diags_phi_rlow.F diags_rho.F do_atmospheric_phys.F do_fields_blocking_exchanges.F do_oceanic_phys.F do_stagger_fields_exchanges.F do_statevars_diags.F do_statevars_tave.F do_the_model_io.F do_write_pickup.F dynamics.F external_fields_load.F external_forcing.F external_forcing_surf.F find_alpha.F find_hyd_press_1d.F find_rho.F forcing_surf_relax.F forward_step.F freesurf_rescale_g.F freeze_surface.F grad_sigma.F gsw_teos10.F impldiff.F ini_cartesian_grid.F ini_cg2d.F ini_cg3d.F ini_cori.F ini_curvilinear_grid.F ini_cylinder_grid.F ini_depths.F ini_dynvars.F ini_eos.F ini_ffields.F ini_fields.F ini_forcing.F ini_global_domain.F ini_grid.F ini_linear_phisurf.F ini_local_grid.F ini_masks_etc.F ini_mixing.F ini_mnc_vars.F ini_model_io.F ini_nh_fields.F ini_nh_vars.F ini_nlfs_vars.F ini_p_ground.F ini_parms.F ini_pressure.F ini_psurf.F ini_salt.F ini_sigma_hfac.F ini_spherical_polar_grid.F ini_theta.F ini_vel.F ini_vertical_grid.F initialise_fixed.F initialise_varia.F integr_continuity.F integrate_for_w.F load_fields_driver.F load_grid_spacing.F load_ref_files.F main_do_loop.F momentum_correction_step.F packages_boot.F packages_check.F packages_error_msg.F packages_init_fixed.F packages_init_variables.F packages_print_msg.F packages_readparms.F packages_unused_msg.F packages_write_pickup.F plot_field.F port_rand.F post_cg3d.F pre_cg3d.F pressure_for_eos.F read_pickup.F remove_mean.F reset_nlfs_vars.F rotate_spherical_polar_grid.F rotate_uv2en.F salt_integrate.F seawater.F set_defaults.F set_grid_factors.F set_parms.F set_ref_state.F solve_for_pressure.F solve_pentadiagonal.F solve_tridiagonal.F solve_uv_tridiago.F state_summary.F swfrac.F taueddy_init_varia.F taueddy_tendency_apply.F temp_integrate.F the_main_loop.F the_model_main.F thermodynamics.F timestep.F timestep_tracer.F timestep_wvel.F tracers_correction_step.F tracers_iigw_correction.F turnoff_model_io.F update_cg2d.F update_etah.F update_etaws.F update_masks_etc.F update_r_star.F update_sigma.F update_surf_dr.F write_grid.F write_pickup.F write_state.F :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/model/src/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/eesupp/inc
 BAR2.h BARRIER.h CPP_EEMACROS.h CPP_EEOPTIONS.h CUMULSUM.h DEF_IN_MAKEFILE.h EEBUFF_SCPU.h EEPARAMS.h EESUPPORT.h EXCH.h GLOBAL_MAX.h GLOBAL_SUM.h MAIN_PDIRECTIVES1.h MAIN_PDIRECTIVES2.h MPI_INFO.h SIGREG.h :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/eesupp/inc/$@ $@; fi

#  These files are linked from /Users/jklymak/MITgcmc66b/MITgcm/model/inc
 CG2D.h CG3D.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYNVARS.h DYU_MACROS.h EOS.h FCORI_MACROS.h FFIELDS.h GRID.h GRID_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h MASKS_MACROS.h MASKW_MACROS.h NH_VARS.h PARAMS.h RAS_MACROS.h RAW_MACROS.h RA_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h RESTART.h SET_GRID.h SOLVE_FOR_PRESSURE.h SOLVE_FOR_PRESSURE3D.h SURFACE.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h THE_MODEL_COMMON_BLOCKS.h XC_MACROS.h YC_MACROS.h :
	if [ ! -L $@ ]; then $(LN) /Users/jklymak/MITgcmc66b/MITgcm/model/inc/$@ $@; fi


# DO NOT DELETE

chksum_tiled.for: DEBUG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
chksum_tiled.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
debug_call.for: DEBUG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
debug_call.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
debug_cs_corner_uv.for: DEBUG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
debug_cs_corner_uv.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
debug_enter.for: DEBUG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
debug_enter.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
debug_fld_stats_rl.for: DEBUG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
debug_fld_stats_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
debug_fld_stats_rs.for: DEBUG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
debug_fld_stats_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
debug_leave.for: DEBUG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
debug_leave.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
debug_msg.for: DEBUG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
debug_msg.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
debug_stats_rl.for: DEBUG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
debug_stats_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
debug_stats_rs.for: DEBUG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
debug_stats_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
fill_in_corners_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
write_fullarray_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
write_fullarray_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diag_calc_psivel.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diag_calc_psivel.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diag_calc_psivel.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
diag_calc_psivel.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
diag_calc_psivel.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
diag_calc_psivel.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
diag_calc_psivel.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
diag_calc_psivel.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
diag_calc_psivel.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
diag_calc_psivel.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
diag_calc_psivel.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
diag_calc_psivel.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
diag_calc_psivel.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
diag_calc_psivel.for: FCORI_MACROS.h OBCS_GRID.h
diag_cg2d.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
diag_cg2d.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
diag_vegtile_fill.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diag_vegtile_fill.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diag_vegtile_fill.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_addtolist.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_addtolist.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_addtolist.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_calc_phivel.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_calc_phivel.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_calc_phivel.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
diagnostics_calc_phivel.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
diagnostics_calc_phivel.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
diagnostics_calc_phivel.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
diagnostics_calc_phivel.for: HFACW_MACROS.h RECIP_DXC_MACROS.h
diagnostics_calc_phivel.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
diagnostics_calc_phivel.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
diagnostics_calc_phivel.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
diagnostics_calc_phivel.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
diagnostics_calc_phivel.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
diagnostics_calc_phivel.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
diagnostics_calc_phivel.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
diagnostics_calc_phivel.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
diagnostics_calc_phivel.for: FCORI_MACROS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_calc_phivel.for: DIAGNOSTICS_CALC.h
diagnostics_check.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_check.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_check.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
diagnostics_check.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
diagnostics_check.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
diagnostics_check.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
diagnostics_check.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
diagnostics_check.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
diagnostics_check.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
diagnostics_check.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
diagnostics_check.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
diagnostics_check.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
diagnostics_check.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
diagnostics_check.for: TANPHIATV_MACROS.h FCORI_MACROS.h DIAGNOSTICS_SIZE.h
diagnostics_check.for: DIAGNOSTICS.h
diagnostics_clear.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_clear.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagnostics_clear.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_fill.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_fill.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagnostics_fill.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_fill_field.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_fill_field.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagnostics_fill_field.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_fill_rs.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_fill_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagnostics_fill_rs.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_fill_state.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_fill_state.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_fill_state.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
diagnostics_fill_state.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
diagnostics_fill_state.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
diagnostics_fill_state.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
diagnostics_fill_state.for: HFACW_MACROS.h RECIP_DXC_MACROS.h
diagnostics_fill_state.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
diagnostics_fill_state.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
diagnostics_fill_state.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
diagnostics_fill_state.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
diagnostics_fill_state.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
diagnostics_fill_state.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
diagnostics_fill_state.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
diagnostics_fill_state.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
diagnostics_fill_state.for: FCORI_MACROS.h SURFACE.h DYNVARS.h NH_VARS.h
diagnostics_fill_state.for: GAD.h
diagnostics_fract_fill.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_fract_fill.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagnostics_fract_fill.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_init_early.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_init_early.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_init_early.for: PARAMS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_init_fixed.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_init_fixed.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagnostics_init_fixed.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_init_varia.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_init_varia.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_init_varia.for: PARAMS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_interp_p2p.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_interp_p2p.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
diagnostics_interp_vert.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_interp_vert.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_interp_vert.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
diagnostics_interp_vert.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
diagnostics_interp_vert.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
diagnostics_interp_vert.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
diagnostics_interp_vert.for: HFACW_MACROS.h RECIP_DXC_MACROS.h
diagnostics_interp_vert.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
diagnostics_interp_vert.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
diagnostics_interp_vert.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
diagnostics_interp_vert.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
diagnostics_interp_vert.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
diagnostics_interp_vert.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
diagnostics_interp_vert.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
diagnostics_interp_vert.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
diagnostics_interp_vert.for: FCORI_MACROS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_is_on.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_is_on.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagnostics_is_on.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_list_check.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_list_check.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_list_check.for: PARAMS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_main_init.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_main_init.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_main_init.for: PARAMS.h
diagnostics_mnc_out.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_mnc_out.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_mnc_out.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
diagnostics_mnc_out.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
diagnostics_mnc_out.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
diagnostics_mnc_out.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
diagnostics_mnc_out.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
diagnostics_mnc_out.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
diagnostics_mnc_out.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
diagnostics_mnc_out.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
diagnostics_mnc_out.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
diagnostics_mnc_out.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
diagnostics_mnc_out.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
diagnostics_mnc_out.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
diagnostics_mnc_out.for: FCORI_MACROS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_out.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_out.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_out.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
diagnostics_out.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
diagnostics_out.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
diagnostics_out.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
diagnostics_out.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
diagnostics_out.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
diagnostics_out.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
diagnostics_out.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
diagnostics_out.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
diagnostics_out.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
diagnostics_out.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_read_pickup.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_read_pickup.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_read_pickup.for: PARAMS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_readparms.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_readparms.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_readparms.for: PARAMS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_readparms.for: DIAGNOSTICS_CALC.h DIAGSTATS_REGIONS.h
diagnostics_scale_fill.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_scale_fill.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagnostics_scale_fill.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_scale_fill_rs.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_scale_fill_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h
diagnostics_scale_fill_rs.for: SIZE.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_set_calc.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_set_calc.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagnostics_set_calc.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
diagnostics_set_calc.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
diagnostics_set_calc.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
diagnostics_set_calc.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
diagnostics_set_calc.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
diagnostics_set_calc.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
diagnostics_set_calc.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
diagnostics_set_calc.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
diagnostics_set_calc.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
diagnostics_set_calc.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
diagnostics_set_calc.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
diagnostics_set_calc.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
diagnostics_set_calc.for: TANPHIATV_MACROS.h FCORI_MACROS.h
diagnostics_set_calc.for: DIAGNOSTICS_CALC.h OBCS_GRID.h
diagnostics_set_levels.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_set_levels.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_set_levels.for: PARAMS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_set_pointers.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_set_pointers.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h
diagnostics_set_pointers.for: SIZE.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_setdiag.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_setdiag.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagnostics_setdiag.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_status_error.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_status_error.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
diagnostics_status_error.for: EEPARAMS.h PARAMS.h DIAGNOSTICS_SIZE.h
diagnostics_status_error.for: DIAGNOSTICS.h
diagnostics_sum_levels.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_sum_levels.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_sum_levels.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
diagnostics_sum_levels.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
diagnostics_sum_levels.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
diagnostics_sum_levels.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
diagnostics_sum_levels.for: HFACW_MACROS.h RECIP_DXC_MACROS.h
diagnostics_sum_levels.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
diagnostics_sum_levels.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
diagnostics_sum_levels.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
diagnostics_sum_levels.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
diagnostics_sum_levels.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
diagnostics_sum_levels.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
diagnostics_sum_levels.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
diagnostics_sum_levels.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
diagnostics_sum_levels.for: FCORI_MACROS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_summary.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_summary.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagnostics_summary.for: PARAMS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_switch_onoff.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_switch_onoff.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
diagnostics_switch_onoff.for: EEPARAMS.h PARAMS.h DIAGNOSTICS_SIZE.h
diagnostics_switch_onoff.for: DIAGNOSTICS.h
diagnostics_utils.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_utils.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagnostics_utils.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagnostics_write.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_write.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagnostics_write.for: DIAGNOSTICS_SIZE.h PARAMS.h DIAGNOSTICS.h
diagnostics_write_pickup.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagnostics_write_pickup.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
diagnostics_write_pickup.for: EEPARAMS.h PARAMS.h DIAGNOSTICS_SIZE.h
diagnostics_write_pickup.for: DIAGNOSTICS.h
diagstats_ascii_out.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_ascii_out.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagstats_ascii_out.for: EESUPPORT.h /usr/local/include/mpif.h
diagstats_ascii_out.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagstats_calc.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_calc.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagstats_clear.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_clear.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagstats_clear.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagstats_close_io.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_close_io.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagstats_close_io.for: PARAMS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagstats_fill.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_fill.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagstats_fill.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagstats_global.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_global.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagstats_global.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagstats_ini_io.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_ini_io.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagstats_ini_io.for: EESUPPORT.h /usr/local/include/mpif.h PARAMS.h
diagstats_ini_io.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagstats_local.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_local.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagstats_local.for: DIAGNOSTICS_SIZE.h DIAGSTATS_REGIONS.h PARAMS.h GRID.h
diagstats_local.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
diagstats_local.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
diagstats_local.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
diagstats_local.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
diagstats_local.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
diagstats_local.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
diagstats_local.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
diagstats_local.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
diagstats_local.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
diagstats_local.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
diagstats_mnc_out.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_mnc_out.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagstats_mnc_out.for: EESUPPORT.h /usr/local/include/mpif.h PARAMS.h GRID.h
diagstats_mnc_out.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
diagstats_mnc_out.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
diagstats_mnc_out.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
diagstats_mnc_out.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
diagstats_mnc_out.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
diagstats_mnc_out.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
diagstats_mnc_out.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
diagstats_mnc_out.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
diagstats_mnc_out.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
diagstats_mnc_out.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
diagstats_mnc_out.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
diagstats_mnc_out.for: FCORI_MACROS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagstats_others_calc.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_others_calc.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagstats_output.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_output.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
diagstats_output.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
diagstats_output.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
diagstats_output.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
diagstats_output.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
diagstats_output.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
diagstats_output.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
diagstats_output.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
diagstats_output.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
diagstats_output.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
diagstats_output.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
diagstats_output.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
diagstats_output.for: FCORI_MACROS.h DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagstats_set_pointers.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_set_pointers.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagstats_set_pointers.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
diagstats_set_pointers.for: DIAGSTATS_REGIONS.h
diagstats_set_regions.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_set_regions.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagstats_set_regions.for: PARAMS.h DIAGNOSTICS_SIZE.h DIAGSTATS_REGIONS.h
diagstats_setdiag.for: DIAG_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
diagstats_setdiag.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
diagstats_setdiag.for: DIAGNOSTICS_SIZE.h DIAGNOSTICS.h
gad_advection.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_advection.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
gad_advection.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
gad_advection.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
gad_advection.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_advection.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_advection.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
gad_advection.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_advection.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_advection.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_advection.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_advection.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_advscheme.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_advscheme.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GAD.h EEPARAMS.h
gad_biharm_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_biharm_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
gad_biharm_r.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_biharm_r.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_biharm_r.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_biharm_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_biharm_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_biharm_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_biharm_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_biharm_r.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_biharm_r.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_biharm_r.for: TANPHIATV_MACROS.h FCORI_MACROS.h
gad_biharm_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_biharm_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_biharm_x.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_biharm_x.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_biharm_x.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_biharm_x.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_biharm_x.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_biharm_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_biharm_x.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_biharm_x.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_biharm_x.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_biharm_x.for: TANPHIATV_MACROS.h FCORI_MACROS.h
gad_biharm_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_biharm_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_biharm_y.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_biharm_y.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_biharm_y.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_biharm_y.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_biharm_y.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_biharm_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_biharm_y.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_biharm_y.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_biharm_y.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_biharm_y.for: TANPHIATV_MACROS.h FCORI_MACROS.h
gad_c2_adv_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_c2_adv_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_c2_adv_r.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_c2_adv_r.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_c2_adv_r.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_c2_adv_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_c2_adv_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_c2_adv_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_c2_adv_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_c2_adv_r.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_c2_adv_r.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_c2_adv_r.for: TANPHIATV_MACROS.h FCORI_MACROS.h EEPARAMS.h PARAMS.h
gad_c2_adv_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_c2_adv_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_c2_adv_x.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_c2_adv_x.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_c2_adv_x.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_c2_adv_x.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_c2_adv_x.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_c2_adv_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_c2_adv_x.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_c2_adv_x.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_c2_adv_x.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_c2_adv_x.for: TANPHIATV_MACROS.h FCORI_MACROS.h
gad_c2_adv_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_c2_adv_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_c2_adv_y.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_c2_adv_y.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_c2_adv_y.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_c2_adv_y.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_c2_adv_y.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_c2_adv_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_c2_adv_y.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_c2_adv_y.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_c2_adv_y.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_c2_adv_y.for: TANPHIATV_MACROS.h FCORI_MACROS.h
gad_c2_impl_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_c2_impl_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_c2_impl_r.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_c2_impl_r.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_c2_impl_r.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_c2_impl_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_c2_impl_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_c2_impl_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_c2_impl_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_c2_impl_r.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_c2_impl_r.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_c2_impl_r.for: TANPHIATV_MACROS.h FCORI_MACROS.h EEPARAMS.h PARAMS.h
gad_c4_adv_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_c4_adv_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_c4_adv_r.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_c4_adv_r.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_c4_adv_r.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_c4_adv_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_c4_adv_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_c4_adv_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_c4_adv_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_c4_adv_r.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_c4_adv_r.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_c4_adv_r.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_c4_adv_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_c4_adv_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_c4_adv_x.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_c4_adv_x.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_c4_adv_x.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_c4_adv_x.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_c4_adv_x.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_c4_adv_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_c4_adv_x.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_c4_adv_x.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_c4_adv_x.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_c4_adv_x.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_c4_adv_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_c4_adv_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_c4_adv_y.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_c4_adv_y.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_c4_adv_y.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_c4_adv_y.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_c4_adv_y.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_c4_adv_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_c4_adv_y.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_c4_adv_y.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_c4_adv_y.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_c4_adv_y.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_calc_rhs.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_calc_rhs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
gad_calc_rhs.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_calc_rhs.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_calc_rhs.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_calc_rhs.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_calc_rhs.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_calc_rhs.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_calc_rhs.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_calc_rhs.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_calc_rhs.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_calc_rhs.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h GAD.h
gad_check.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
gad_check.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GAD.h
gad_del2.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
gad_del2.for: CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h DXC_MACROS.h
gad_del2.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
gad_del2.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
gad_del2.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
gad_del2.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_del2.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
gad_del2.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_del2.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_del2.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_del2.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gad_diagnostics_init.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_diagnostics_init.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
gad_diagnostics_init.for: PARAMS.h GAD.h
gad_diagnostics_state.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_diagnostics_state.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
gad_diagnostics_state.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
gad_diagnostics_state.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_diagnostics_state.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_diagnostics_state.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_diagnostics_state.for: HFACW_MACROS.h RECIP_DXC_MACROS.h
gad_diagnostics_state.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_diagnostics_state.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
gad_diagnostics_state.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
gad_diagnostics_state.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_diagnostics_state.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
gad_diagnostics_state.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
gad_diagnostics_state.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_diagnostics_state.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
gad_diagnostics_state.for: FCORI_MACROS.h GAD.h GAD_SOM_VARS.h
gad_diff_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
gad_diff_r.for: CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h DXC_MACROS.h
gad_diff_r.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
gad_diff_r.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
gad_diff_r.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
gad_diff_r.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_diff_r.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
gad_diff_r.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_diff_r.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_diff_r.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_diff_r.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gad_diff_r.for: EEPARAMS.h PARAMS.h
gad_diff_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
gad_diff_x.for: CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h DXC_MACROS.h
gad_diff_x.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
gad_diff_x.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
gad_diff_x.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
gad_diff_x.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_diff_x.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
gad_diff_x.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_diff_x.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_diff_x.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_diff_x.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gad_diff_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
gad_diff_y.for: CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h DXC_MACROS.h
gad_diff_y.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
gad_diff_y.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
gad_diff_y.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
gad_diff_y.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_diff_y.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
gad_diff_y.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_diff_y.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_diff_y.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_diff_y.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gad_dst2u1_adv_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_dst2u1_adv_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_dst2u1_adv_r.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_dst2u1_adv_r.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_dst2u1_adv_r.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_dst2u1_adv_r.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_dst2u1_adv_r.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_dst2u1_adv_r.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_dst2u1_adv_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_dst2u1_adv_r.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_dst2u1_adv_r.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
gad_dst2u1_adv_r.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
gad_dst2u1_adv_r.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
gad_dst2u1_adv_r.for: FCORI_MACROS.h GAD.h
gad_dst2u1_adv_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_dst2u1_adv_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_dst2u1_adv_x.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_dst2u1_adv_x.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_dst2u1_adv_x.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_dst2u1_adv_x.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_dst2u1_adv_x.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_dst2u1_adv_x.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_dst2u1_adv_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_dst2u1_adv_x.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_dst2u1_adv_x.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
gad_dst2u1_adv_x.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
gad_dst2u1_adv_x.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
gad_dst2u1_adv_x.for: FCORI_MACROS.h GAD.h
gad_dst2u1_adv_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_dst2u1_adv_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_dst2u1_adv_y.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_dst2u1_adv_y.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_dst2u1_adv_y.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_dst2u1_adv_y.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_dst2u1_adv_y.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_dst2u1_adv_y.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_dst2u1_adv_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_dst2u1_adv_y.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_dst2u1_adv_y.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
gad_dst2u1_adv_y.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
gad_dst2u1_adv_y.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
gad_dst2u1_adv_y.for: FCORI_MACROS.h GAD.h
gad_dst2u1_impl_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_dst2u1_impl_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_dst2u1_impl_r.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_dst2u1_impl_r.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_dst2u1_impl_r.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_dst2u1_impl_r.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_dst2u1_impl_r.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_dst2u1_impl_r.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_dst2u1_impl_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_dst2u1_impl_r.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_dst2u1_impl_r.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
gad_dst2u1_impl_r.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
gad_dst2u1_impl_r.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
gad_dst2u1_impl_r.for: FCORI_MACROS.h EEPARAMS.h PARAMS.h GAD.h
gad_dst3_adv_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_dst3_adv_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_dst3_adv_r.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_dst3_adv_r.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_dst3_adv_r.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_dst3_adv_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_dst3_adv_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_dst3_adv_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_dst3_adv_r.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_dst3_adv_r.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_dst3_adv_r.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_dst3_adv_r.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gad_dst3_adv_r.for: GAD.h
gad_dst3_adv_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_dst3_adv_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_dst3_adv_x.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_dst3_adv_x.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_dst3_adv_x.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_dst3_adv_x.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_dst3_adv_x.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_dst3_adv_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_dst3_adv_x.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_dst3_adv_x.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_dst3_adv_x.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_dst3_adv_x.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gad_dst3_adv_x.for: GAD.h
gad_dst3_adv_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_dst3_adv_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_dst3_adv_y.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_dst3_adv_y.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_dst3_adv_y.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_dst3_adv_y.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_dst3_adv_y.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_dst3_adv_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_dst3_adv_y.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_dst3_adv_y.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_dst3_adv_y.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_dst3_adv_y.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gad_dst3_adv_y.for: GAD.h
gad_dst3fl_adv_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_dst3fl_adv_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_dst3fl_adv_r.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_dst3fl_adv_r.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_dst3fl_adv_r.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_dst3fl_adv_r.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_dst3fl_adv_r.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_dst3fl_adv_r.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_dst3fl_adv_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_dst3fl_adv_r.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_dst3fl_adv_r.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
gad_dst3fl_adv_r.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
gad_dst3fl_adv_r.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
gad_dst3fl_adv_r.for: FCORI_MACROS.h GAD.h
gad_dst3fl_adv_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_dst3fl_adv_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_dst3fl_adv_x.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_dst3fl_adv_x.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_dst3fl_adv_x.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_dst3fl_adv_x.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_dst3fl_adv_x.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_dst3fl_adv_x.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_dst3fl_adv_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_dst3fl_adv_x.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_dst3fl_adv_x.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
gad_dst3fl_adv_x.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
gad_dst3fl_adv_x.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
gad_dst3fl_adv_x.for: FCORI_MACROS.h GAD.h
gad_dst3fl_adv_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_dst3fl_adv_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_dst3fl_adv_y.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_dst3fl_adv_y.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_dst3fl_adv_y.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_dst3fl_adv_y.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_dst3fl_adv_y.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_dst3fl_adv_y.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_dst3fl_adv_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_dst3fl_adv_y.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_dst3fl_adv_y.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
gad_dst3fl_adv_y.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
gad_dst3fl_adv_y.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
gad_dst3fl_adv_y.for: FCORI_MACROS.h GAD.h
gad_dst3fl_impl_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_dst3fl_impl_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_dst3fl_impl_r.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_dst3fl_impl_r.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_dst3fl_impl_r.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_dst3fl_impl_r.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_dst3fl_impl_r.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_dst3fl_impl_r.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_dst3fl_impl_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_dst3fl_impl_r.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_dst3fl_impl_r.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
gad_dst3fl_impl_r.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
gad_dst3fl_impl_r.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
gad_dst3fl_impl_r.for: FCORI_MACROS.h EEPARAMS.h PARAMS.h GAD.h
gad_exch_som.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_exch_som.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h GAD.h
gad_fluxlimit_adv_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_fluxlimit_adv_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_fluxlimit_adv_r.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_fluxlimit_adv_r.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_fluxlimit_adv_r.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_fluxlimit_adv_r.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_fluxlimit_adv_r.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_fluxlimit_adv_r.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_fluxlimit_adv_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_fluxlimit_adv_r.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_fluxlimit_adv_r.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
gad_fluxlimit_adv_r.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
gad_fluxlimit_adv_r.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
gad_fluxlimit_adv_r.for: FCORI_MACROS.h EEPARAMS.h PARAMS.h
gad_fluxlimit_adv_r.for: GAD_FLUX_LIMITER.h
gad_fluxlimit_adv_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_fluxlimit_adv_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_fluxlimit_adv_x.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_fluxlimit_adv_x.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_fluxlimit_adv_x.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_fluxlimit_adv_x.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_fluxlimit_adv_x.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_fluxlimit_adv_x.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_fluxlimit_adv_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_fluxlimit_adv_x.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_fluxlimit_adv_x.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
gad_fluxlimit_adv_x.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
gad_fluxlimit_adv_x.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
gad_fluxlimit_adv_x.for: FCORI_MACROS.h GAD_FLUX_LIMITER.h
gad_fluxlimit_adv_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_fluxlimit_adv_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_fluxlimit_adv_y.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_fluxlimit_adv_y.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_fluxlimit_adv_y.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_fluxlimit_adv_y.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_fluxlimit_adv_y.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
gad_fluxlimit_adv_y.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_fluxlimit_adv_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_fluxlimit_adv_y.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_fluxlimit_adv_y.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
gad_fluxlimit_adv_y.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
gad_fluxlimit_adv_y.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
gad_fluxlimit_adv_y.for: FCORI_MACROS.h GAD_FLUX_LIMITER.h
gad_fluxlimit_impl_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_fluxlimit_impl_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_fluxlimit_impl_r.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
gad_fluxlimit_impl_r.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
gad_fluxlimit_impl_r.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
gad_fluxlimit_impl_r.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
gad_fluxlimit_impl_r.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_fluxlimit_impl_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
gad_fluxlimit_impl_r.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
gad_fluxlimit_impl_r.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_fluxlimit_impl_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
gad_fluxlimit_impl_r.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
gad_fluxlimit_impl_r.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_fluxlimit_impl_r.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
gad_fluxlimit_impl_r.for: FCORI_MACROS.h EEPARAMS.h PARAMS.h
gad_fluxlimit_impl_r.for: GAD_FLUX_LIMITER.h
gad_grad_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
gad_grad_x.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h GRID.h GRID_MACROS.h
gad_grad_x.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_grad_x.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_grad_x.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_grad_x.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_grad_x.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_grad_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_grad_x.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_grad_x.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_grad_x.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_grad_x.for: TANPHIATV_MACROS.h FCORI_MACROS.h
gad_grad_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
gad_grad_y.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h GRID.h GRID_MACROS.h
gad_grad_y.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_grad_y.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_grad_y.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_grad_y.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_grad_y.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_grad_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_grad_y.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_grad_y.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_grad_y.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_grad_y.for: TANPHIATV_MACROS.h FCORI_MACROS.h
gad_implicit_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_implicit_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
gad_implicit_r.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
gad_implicit_r.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
gad_implicit_r.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_implicit_r.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_implicit_r.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
gad_implicit_r.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_implicit_r.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_implicit_r.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_implicit_r.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_implicit_r.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gad_implicit_r.for: SURFACE.h GAD.h
gad_init_fixed.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_init_fixed.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
gad_init_fixed.for: GAD.h
gad_init_varia.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_init_varia.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
gad_init_varia.for: GAD.h GAD_SOM_VARS.h
gad_os7mp_adv_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_os7mp_adv_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_os7mp_adv_r.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_os7mp_adv_r.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_os7mp_adv_r.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_os7mp_adv_r.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_os7mp_adv_r.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
gad_os7mp_adv_r.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_os7mp_adv_r.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_os7mp_adv_r.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_os7mp_adv_r.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_os7mp_adv_r.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gad_os7mp_adv_r.for: GAD.h
gad_os7mp_adv_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_os7mp_adv_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_os7mp_adv_x.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_os7mp_adv_x.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_os7mp_adv_x.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_os7mp_adv_x.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_os7mp_adv_x.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
gad_os7mp_adv_x.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_os7mp_adv_x.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_os7mp_adv_x.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_os7mp_adv_x.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_os7mp_adv_x.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gad_os7mp_adv_x.for: GAD.h
gad_os7mp_adv_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_os7mp_adv_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_os7mp_adv_y.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_os7mp_adv_y.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_os7mp_adv_y.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_os7mp_adv_y.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_os7mp_adv_y.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
gad_os7mp_adv_y.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_os7mp_adv_y.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_os7mp_adv_y.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_os7mp_adv_y.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_os7mp_adv_y.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gad_os7mp_adv_y.for: GAD.h
gad_osc_hat_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_osc_hat_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
gad_osc_hat_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_osc_hat_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
gad_osc_hat_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_osc_hat_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
gad_osc_mul_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_osc_mul_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
gad_osc_mul_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_osc_mul_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
gad_osc_mul_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_osc_mul_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
gad_plm_fun.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_plm_fun.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
gad_ppm_adv_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_ppm_adv_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_ppm_adv_r.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_ppm_adv_r.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_ppm_adv_r.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_ppm_adv_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_ppm_adv_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_ppm_adv_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_ppm_adv_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_ppm_adv_r.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_ppm_adv_r.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_ppm_adv_r.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_ppm_adv_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_ppm_adv_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_ppm_adv_x.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_ppm_adv_x.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_ppm_adv_x.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_ppm_adv_x.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_ppm_adv_x.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_ppm_adv_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_ppm_adv_x.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_ppm_adv_x.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_ppm_adv_x.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_ppm_adv_x.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_ppm_adv_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_ppm_adv_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_ppm_adv_y.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_ppm_adv_y.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_ppm_adv_y.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_ppm_adv_y.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_ppm_adv_y.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_ppm_adv_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_ppm_adv_y.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_ppm_adv_y.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_ppm_adv_y.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_ppm_adv_y.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_ppm_flx_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_ppm_flx_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_ppm_flx_r.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_ppm_flx_r.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_ppm_flx_r.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_ppm_flx_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_ppm_flx_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_ppm_flx_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_ppm_flx_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_ppm_flx_r.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_ppm_flx_r.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_ppm_flx_r.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_ppm_flx_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_ppm_flx_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_ppm_flx_x.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_ppm_flx_x.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_ppm_flx_x.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_ppm_flx_x.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_ppm_flx_x.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_ppm_flx_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_ppm_flx_x.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_ppm_flx_x.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_ppm_flx_x.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_ppm_flx_x.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_ppm_flx_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_ppm_flx_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_ppm_flx_y.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_ppm_flx_y.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_ppm_flx_y.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_ppm_flx_y.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_ppm_flx_y.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_ppm_flx_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_ppm_flx_y.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_ppm_flx_y.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_ppm_flx_y.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_ppm_flx_y.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_ppm_fun.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_ppm_fun.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
gad_ppm_hat_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_ppm_hat_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_ppm_hat_r.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_ppm_hat_r.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_ppm_hat_r.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_ppm_hat_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_ppm_hat_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_ppm_hat_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_ppm_hat_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_ppm_hat_r.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_ppm_hat_r.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_ppm_hat_r.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_ppm_hat_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_ppm_hat_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_ppm_hat_x.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_ppm_hat_x.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_ppm_hat_x.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_ppm_hat_x.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_ppm_hat_x.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_ppm_hat_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_ppm_hat_x.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_ppm_hat_x.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_ppm_hat_x.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_ppm_hat_x.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_ppm_hat_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_ppm_hat_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_ppm_hat_y.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_ppm_hat_y.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_ppm_hat_y.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_ppm_hat_y.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_ppm_hat_y.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_ppm_hat_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_ppm_hat_y.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_ppm_hat_y.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_ppm_hat_y.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_ppm_hat_y.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_ppm_p3e_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_ppm_p3e_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_ppm_p3e_r.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_ppm_p3e_r.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_ppm_p3e_r.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_ppm_p3e_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_ppm_p3e_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_ppm_p3e_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_ppm_p3e_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_ppm_p3e_r.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_ppm_p3e_r.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_ppm_p3e_r.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_ppm_p3e_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_ppm_p3e_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_ppm_p3e_x.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_ppm_p3e_x.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_ppm_p3e_x.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_ppm_p3e_x.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_ppm_p3e_x.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_ppm_p3e_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_ppm_p3e_x.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_ppm_p3e_x.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_ppm_p3e_x.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_ppm_p3e_x.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_ppm_p3e_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_ppm_p3e_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_ppm_p3e_y.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_ppm_p3e_y.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_ppm_p3e_y.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_ppm_p3e_y.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_ppm_p3e_y.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_ppm_p3e_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_ppm_p3e_y.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_ppm_p3e_y.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_ppm_p3e_y.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_ppm_p3e_y.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_pqm_adv_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_pqm_adv_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_pqm_adv_r.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_pqm_adv_r.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_pqm_adv_r.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_pqm_adv_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_pqm_adv_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_pqm_adv_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_pqm_adv_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_pqm_adv_r.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_pqm_adv_r.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_pqm_adv_r.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_pqm_adv_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_pqm_adv_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_pqm_adv_x.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_pqm_adv_x.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_pqm_adv_x.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_pqm_adv_x.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_pqm_adv_x.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_pqm_adv_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_pqm_adv_x.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_pqm_adv_x.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_pqm_adv_x.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_pqm_adv_x.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_pqm_adv_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_pqm_adv_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_pqm_adv_y.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_pqm_adv_y.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_pqm_adv_y.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_pqm_adv_y.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_pqm_adv_y.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_pqm_adv_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_pqm_adv_y.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_pqm_adv_y.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_pqm_adv_y.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_pqm_adv_y.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_pqm_flx_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_pqm_flx_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_pqm_flx_r.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_pqm_flx_r.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_pqm_flx_r.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_pqm_flx_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_pqm_flx_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_pqm_flx_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_pqm_flx_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_pqm_flx_r.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_pqm_flx_r.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_pqm_flx_r.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_pqm_flx_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_pqm_flx_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_pqm_flx_x.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_pqm_flx_x.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_pqm_flx_x.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_pqm_flx_x.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_pqm_flx_x.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_pqm_flx_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_pqm_flx_x.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_pqm_flx_x.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_pqm_flx_x.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_pqm_flx_x.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_pqm_flx_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_pqm_flx_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_pqm_flx_y.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_pqm_flx_y.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_pqm_flx_y.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_pqm_flx_y.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_pqm_flx_y.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_pqm_flx_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_pqm_flx_y.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_pqm_flx_y.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_pqm_flx_y.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_pqm_flx_y.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_pqm_fun.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_pqm_fun.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
gad_pqm_hat_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_pqm_hat_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_pqm_hat_r.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_pqm_hat_r.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_pqm_hat_r.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_pqm_hat_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_pqm_hat_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_pqm_hat_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_pqm_hat_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_pqm_hat_r.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_pqm_hat_r.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_pqm_hat_r.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_pqm_hat_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_pqm_hat_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_pqm_hat_x.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_pqm_hat_x.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_pqm_hat_x.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_pqm_hat_x.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_pqm_hat_x.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_pqm_hat_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_pqm_hat_x.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_pqm_hat_x.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_pqm_hat_x.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_pqm_hat_x.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_pqm_hat_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_pqm_hat_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_pqm_hat_y.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_pqm_hat_y.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_pqm_hat_y.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_pqm_hat_y.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_pqm_hat_y.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_pqm_hat_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_pqm_hat_y.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_pqm_hat_y.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_pqm_hat_y.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_pqm_hat_y.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_pqm_p5e_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_pqm_p5e_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_pqm_p5e_r.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_pqm_p5e_r.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_pqm_p5e_r.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_pqm_p5e_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_pqm_p5e_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_pqm_p5e_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_pqm_p5e_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_pqm_p5e_r.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_pqm_p5e_r.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_pqm_p5e_r.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_pqm_p5e_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_pqm_p5e_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_pqm_p5e_x.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_pqm_p5e_x.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_pqm_p5e_x.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_pqm_p5e_x.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_pqm_p5e_x.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_pqm_p5e_x.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_pqm_p5e_x.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_pqm_p5e_x.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_pqm_p5e_x.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_pqm_p5e_x.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_pqm_p5e_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_pqm_p5e_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_pqm_p5e_y.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_pqm_p5e_y.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_pqm_p5e_y.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_pqm_p5e_y.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_pqm_p5e_y.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_pqm_p5e_y.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_pqm_p5e_y.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_pqm_p5e_y.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_pqm_p5e_y.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_pqm_p5e_y.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_read_pickup.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_read_pickup.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
gad_read_pickup.for: PARAMS.h GAD.h GAD_SOM_VARS.h
gad_som_adv_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_som_adv_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
gad_som_adv_r.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
gad_som_adv_r.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
gad_som_adv_r.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_som_adv_r.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_som_adv_r.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
gad_som_adv_r.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_som_adv_r.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_som_adv_r.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_som_adv_r.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_som_adv_r.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_som_adv_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_som_adv_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h GAD.h
gad_som_adv_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_som_adv_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h GAD.h
gad_som_advect.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_som_advect.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
gad_som_advect.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
gad_som_advect.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
gad_som_advect.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_som_advect.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_som_advect.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
gad_som_advect.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_som_advect.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_som_advect.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_som_advect.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_som_advect.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gad_som_advect.for: GAD.h
gad_som_exchanges.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_som_exchanges.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h GAD.h
gad_som_exchanges.for: GAD_SOM_VARS.h
gad_som_fill_cs_corner.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_som_fill_cs_corner.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
gad_som_fill_cs_corner.for: PARAMS.h GAD.h
gad_som_lim_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_som_lim_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GAD.h
gad_som_prep_cs_corner.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_som_prep_cs_corner.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
gad_som_prep_cs_corner.for: GAD.h
gad_u3_adv_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_u3_adv_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
gad_u3_adv_r.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
gad_u3_adv_r.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
gad_u3_adv_r.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
gad_u3_adv_r.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
gad_u3_adv_r.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
gad_u3_adv_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
gad_u3_adv_r.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
gad_u3_adv_r.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
gad_u3_adv_r.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
gad_u3_adv_r.for: TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
gad_u3_adv_x.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_u3_adv_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GAD.h
gad_u3_adv_y.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_u3_adv_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GAD.h
gad_u3c4_impl_r.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_u3c4_impl_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
gad_u3c4_impl_r.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
gad_u3c4_impl_r.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
gad_u3c4_impl_r.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
gad_u3c4_impl_r.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
gad_u3c4_impl_r.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
gad_u3c4_impl_r.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
gad_u3c4_impl_r.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
gad_u3c4_impl_r.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
gad_u3c4_impl_r.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
gad_u3c4_impl_r.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gad_u3c4_impl_r.for: EEPARAMS.h PARAMS.h GAD.h
gad_write_pickup.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
gad_write_pickup.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
gad_write_pickup.for: PARAMS.h GAD.h GAD_SOM_VARS.h
salt_fill.for: GAD_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
salt_fill.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h
salt_fill.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
salt_fill.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
salt_fill.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
salt_fill.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
salt_fill.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
salt_fill.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
salt_fill.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
salt_fill.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
salt_fill.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
salt_fill.for: TANPHIATV_MACROS.h FCORI_MACROS.h
kl10_calc.for: KL10_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
kl10_calc.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h EOS.h GRID.h
kl10_calc.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
kl10_calc.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
kl10_calc.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
kl10_calc.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
kl10_calc.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
kl10_calc.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
kl10_calc.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
kl10_calc.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
kl10_calc.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
kl10_calc.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h FFIELDS.h KL10.h
kl10_calc_diff.for: KL10_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
kl10_calc_diff.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
kl10_calc_diff.for: KL10.h
kl10_calc_visc.for: KL10_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
kl10_calc_visc.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
kl10_calc_visc.for: DYNVARS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
kl10_calc_visc.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
kl10_calc_visc.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
kl10_calc_visc.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
kl10_calc_visc.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
kl10_calc_visc.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
kl10_calc_visc.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
kl10_calc_visc.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
kl10_calc_visc.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
kl10_calc_visc.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
kl10_calc_visc.for: KL10.h
kl10_check.for: KL10_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
kl10_check.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
kl10_diagnostics_init.for: KL10_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
kl10_diagnostics_init.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
kl10_init_fixed.for: KL10_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
kl10_init_fixed.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
kl10_init_fixed.for: PARAMS.h
kl10_init_varia.for: KL10_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
kl10_init_varia.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
kl10_init_varia.for: PARAMS.h KL10.h
kl10_output.for: KL10_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
kl10_output.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
kl10_output.for: KL10.h KL10_TAVE.h
kl10_readparms.for: KL10_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
kl10_readparms.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h KL10.h
kl10_readparms.for: PARAMS.h
mdsio_buffertorl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
mdsio_buffertors.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
mdsio_check4file.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_check4file.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_check4file.for: PARAMS.h
mdsio_facef_read.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_facef_read.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_gl.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
mdsio_gl.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mdsio_gl_slice.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_gl_slice.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mdsio_pass_r4torl.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_pass_r4torl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
mdsio_pass_r4tors.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_pass_r4tors.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
mdsio_pass_r8torl.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_pass_r8torl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
mdsio_pass_r8tors.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_pass_r8tors.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
mdsio_rd_rec_rl.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_rd_rec_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
mdsio_rd_rec_rl.for: PARAMS.h
mdsio_rd_rec_rs.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_rd_rec_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
mdsio_rd_rec_rs.for: PARAMS.h
mdsio_read_field.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_read_field.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_read_field.for: PARAMS.h EEBUFF_SCPU.h MDSIO_BUFF_3D.h
mdsio_read_meta.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_read_meta.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_read_meta.for: PARAMS.h
mdsio_read_section.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_read_section.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_read_section.for: PARAMS.h
mdsio_read_tape.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_read_tape.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_read_tape.for: PARAMS.h
mdsio_read_whalos.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_read_whalos.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
mdsio_read_whalos.for: PARAMS.h
mdsio_readvec_loc.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_readvec_loc.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_readvec_loc.for: PARAMS.h MDSIO_BUFF_3D.h
mdsio_rw_field.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_rw_field.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
mdsio_rw_slice.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_rw_slice.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
mdsio_seg4torl.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_seg4torl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
mdsio_seg4tors.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_seg4tors.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
mdsio_seg8torl.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_seg8torl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
mdsio_seg8tors.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_seg8tors.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
mdsio_segxtorx_2d.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_segxtorx_2d.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
mdsio_wr_metafiles.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_wr_metafiles.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_wr_metafiles.for: PARAMS.h
mdsio_wr_rec_rl.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_wr_rec_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
mdsio_wr_rec_rl.for: PARAMS.h
mdsio_wr_rec_rs.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_wr_rec_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
mdsio_wr_rec_rs.for: PARAMS.h
mdsio_write_field.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_write_field.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_write_field.for: PARAMS.h EEBUFF_SCPU.h MDSIO_BUFF_3D.h
mdsio_write_meta.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_write_meta.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_write_section.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_write_section.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_write_section.for: PARAMS.h
mdsio_write_tape.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_write_tape.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_write_tape.for: PARAMS.h
mdsio_write_whalos.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_write_whalos.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h SIZE.h
mdsio_write_whalos.for: PARAMS.h
mdsio_writelocal.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_writelocal.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_writelocal.for: PARAMS.h MDSIO_BUFF_3D.h
mdsio_writevec_loc.for: MDSIO_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mdsio_writevec_loc.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsio_writevec_loc.for: PARAMS.h MDSIO_BUFF_3D.h
mom_calc_3d_strain.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_calc_3d_strain.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_calc_3d_strain.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
mom_calc_3d_strain.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
mom_calc_3d_strain.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_calc_3d_strain.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_calc_3d_strain.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_calc_3d_strain.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_calc_3d_strain.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_calc_3d_strain.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_calc_3d_strain.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_calc_3d_strain.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_calc_3d_strain.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_calc_3d_strain.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
mom_calc_absvort3.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_calc_absvort3.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_calc_absvort3.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
mom_calc_absvort3.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
mom_calc_absvort3.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_calc_absvort3.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_calc_absvort3.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_calc_absvort3.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_calc_absvort3.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_calc_absvort3.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_calc_absvort3.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_calc_absvort3.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_calc_absvort3.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_calc_absvort3.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_calc_hdiv.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_calc_hdiv.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_calc_hdiv.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_calc_hdiv.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_calc_hdiv.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_calc_hdiv.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_calc_hdiv.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_calc_hdiv.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_calc_hdiv.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_calc_hdiv.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_calc_hdiv.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_calc_hdiv.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_calc_hfacz.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_calc_hfacz.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_calc_hfacz.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_calc_hfacz.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_calc_hfacz.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_calc_hfacz.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_calc_hfacz.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_calc_hfacz.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_calc_hfacz.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_calc_hfacz.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_calc_hfacz.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_calc_hfacz.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_calc_ke.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_calc_ke.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
mom_calc_ke.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
mom_calc_ke.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
mom_calc_ke.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_calc_ke.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_calc_ke.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_calc_ke.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_calc_ke.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_calc_ke.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_calc_ke.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_calc_ke.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_calc_relvort3.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_calc_relvort3.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_calc_relvort3.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
mom_calc_relvort3.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
mom_calc_relvort3.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_calc_relvort3.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_calc_relvort3.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_calc_relvort3.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_calc_relvort3.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_calc_relvort3.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_calc_relvort3.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_calc_relvort3.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_calc_relvort3.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_calc_relvort3.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_calc_smag_3d.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_calc_smag_3d.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_calc_smag_3d.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_calc_smag_3d.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_calc_smag_3d.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_calc_smag_3d.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_calc_smag_3d.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_calc_smag_3d.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_calc_smag_3d.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_calc_smag_3d.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_calc_smag_3d.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
mom_calc_smag_3d.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
mom_calc_smag_3d.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
mom_calc_smag_3d.for: FCORI_MACROS.h
mom_calc_strain.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_calc_strain.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_calc_strain.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_calc_strain.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_calc_strain.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_calc_strain.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_calc_strain.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_calc_strain.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_calc_strain.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_calc_strain.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_calc_strain.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_calc_strain.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_calc_tension.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_calc_tension.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_calc_tension.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_calc_tension.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_calc_tension.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_calc_tension.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_calc_tension.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_calc_tension.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_calc_tension.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_calc_tension.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_calc_tension.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
mom_calc_tension.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
mom_calc_tension.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
mom_calc_tension.for: FCORI_MACROS.h
mom_calc_visc.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_calc_visc.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
mom_calc_visc.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
mom_calc_visc.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
mom_calc_visc.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_calc_visc.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_calc_visc.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_calc_visc.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_calc_visc.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_calc_visc.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_calc_visc.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_calc_visc.for: TANPHIATV_MACROS.h FCORI_MACROS.h EEPARAMS.h PARAMS.h
mom_calc_visc.for: MOM_VISC.h
mom_diagnostics_init.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h
mom_diagnostics_init.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
mom_diagnostics_init.for: EEPARAMS.h PARAMS.h
mom_hdissip.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_hdissip.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_hdissip.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_hdissip.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
mom_hdissip.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_hdissip.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_hdissip.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_hdissip.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_hdissip.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_hdissip.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_hdissip.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_hdissip.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_init_fixed.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_init_fixed.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_init_fixed.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_init_fixed.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_init_fixed.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_init_fixed.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_init_fixed.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_init_fixed.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_init_fixed.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_init_fixed.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_init_fixed.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_init_fixed.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_init_fixed.for: SURFACE.h MOM_VISC.h
mom_quasihydrostatic.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h
mom_quasihydrostatic.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
mom_quasihydrostatic.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h
mom_quasihydrostatic.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
mom_quasihydrostatic.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
mom_quasihydrostatic.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_quasihydrostatic.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_quasihydrostatic.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_quasihydrostatic.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_quasihydrostatic.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_quasihydrostatic.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_quasihydrostatic.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
mom_quasihydrostatic.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_quasihydrostatic.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_quasihydrostatic.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_u_botdrag_impl.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_botdrag_impl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_u_botdrag_impl.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
mom_u_botdrag_impl.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
mom_u_botdrag_impl.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_u_botdrag_impl.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_u_botdrag_impl.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_u_botdrag_impl.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_u_botdrag_impl.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_u_botdrag_impl.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_u_botdrag_impl.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_u_botdrag_impl.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_u_botdrag_impl.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_u_botdrag_impl.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_u_bottomdrag.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_bottomdrag.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_u_bottomdrag.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_u_bottomdrag.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_u_bottomdrag.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_u_bottomdrag.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_u_bottomdrag.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_u_bottomdrag.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_u_bottomdrag.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_u_bottomdrag.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_u_bottomdrag.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
mom_u_bottomdrag.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
mom_u_bottomdrag.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
mom_u_bottomdrag.for: FCORI_MACROS.h
mom_u_coriolis_nh.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_coriolis_nh.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_u_coriolis_nh.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
mom_u_coriolis_nh.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
mom_u_coriolis_nh.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_u_coriolis_nh.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_u_coriolis_nh.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_u_coriolis_nh.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_u_coriolis_nh.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_u_coriolis_nh.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_u_coriolis_nh.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_u_coriolis_nh.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_u_coriolis_nh.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_u_coriolis_nh.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_u_implicit_r.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_implicit_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_u_implicit_r.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_u_implicit_r.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_u_implicit_r.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_u_implicit_r.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_u_implicit_r.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_u_implicit_r.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_u_implicit_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_u_implicit_r.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_u_implicit_r.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
mom_u_implicit_r.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
mom_u_implicit_r.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
mom_u_implicit_r.for: FCORI_MACROS.h DYNVARS.h
mom_u_metric_nh.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_metric_nh.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_u_metric_nh.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_u_metric_nh.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_u_metric_nh.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_u_metric_nh.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_u_metric_nh.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_u_metric_nh.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_u_metric_nh.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_u_metric_nh.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_u_metric_nh.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_u_metric_nh.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_u_rviscflux.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_rviscflux.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_u_rviscflux.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_u_rviscflux.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_u_rviscflux.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_u_rviscflux.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_u_rviscflux.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_u_rviscflux.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_u_rviscflux.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_u_rviscflux.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_u_rviscflux.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_u_rviscflux.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_u_sidedrag.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_sidedrag.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_u_sidedrag.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_u_sidedrag.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_u_sidedrag.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_u_sidedrag.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_u_sidedrag.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_u_sidedrag.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_u_sidedrag.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_u_sidedrag.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_u_sidedrag.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_u_sidedrag.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_u_sidedrag.for: SURFACE.h
mom_uv_smag_3d.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_uv_smag_3d.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h GRID.h
mom_uv_smag_3d.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_uv_smag_3d.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
mom_uv_smag_3d.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_uv_smag_3d.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_uv_smag_3d.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_uv_smag_3d.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_uv_smag_3d.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_uv_smag_3d.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_uv_smag_3d.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_uv_smag_3d.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_uv_smag_3d.for: PARAMS.h
mom_v_botdrag_impl.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_botdrag_impl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_v_botdrag_impl.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
mom_v_botdrag_impl.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
mom_v_botdrag_impl.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_v_botdrag_impl.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_v_botdrag_impl.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_v_botdrag_impl.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_v_botdrag_impl.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_v_botdrag_impl.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_v_botdrag_impl.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_v_botdrag_impl.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_v_botdrag_impl.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_v_botdrag_impl.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_v_bottomdrag.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_bottomdrag.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_v_bottomdrag.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_v_bottomdrag.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_v_bottomdrag.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_v_bottomdrag.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_v_bottomdrag.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_v_bottomdrag.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_v_bottomdrag.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_v_bottomdrag.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_v_bottomdrag.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
mom_v_bottomdrag.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
mom_v_bottomdrag.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
mom_v_bottomdrag.for: FCORI_MACROS.h
mom_v_coriolis_nh.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_coriolis_nh.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_v_coriolis_nh.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
mom_v_coriolis_nh.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
mom_v_coriolis_nh.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_v_coriolis_nh.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_v_coriolis_nh.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_v_coriolis_nh.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_v_coriolis_nh.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_v_coriolis_nh.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_v_coriolis_nh.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_v_coriolis_nh.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_v_coriolis_nh.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_v_coriolis_nh.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_v_implicit_r.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_implicit_r.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_v_implicit_r.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_v_implicit_r.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_v_implicit_r.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_v_implicit_r.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_v_implicit_r.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_v_implicit_r.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_v_implicit_r.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_v_implicit_r.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_v_implicit_r.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
mom_v_implicit_r.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
mom_v_implicit_r.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
mom_v_implicit_r.for: FCORI_MACROS.h DYNVARS.h
mom_v_metric_nh.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_metric_nh.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_v_metric_nh.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_v_metric_nh.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_v_metric_nh.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_v_metric_nh.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_v_metric_nh.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_v_metric_nh.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_v_metric_nh.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_v_metric_nh.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_v_metric_nh.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_v_metric_nh.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_v_rviscflux.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_rviscflux.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_v_rviscflux.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_v_rviscflux.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_v_rviscflux.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_v_rviscflux.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_v_rviscflux.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_v_rviscflux.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_v_rviscflux.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_v_rviscflux.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_v_rviscflux.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_v_rviscflux.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_v_sidedrag.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_sidedrag.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_v_sidedrag.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_v_sidedrag.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_v_sidedrag.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_v_sidedrag.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_v_sidedrag.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_v_sidedrag.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_v_sidedrag.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_v_sidedrag.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_v_sidedrag.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_v_sidedrag.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_v_sidedrag.for: SURFACE.h
mom_w_coriolis_nh.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_w_coriolis_nh.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_w_coriolis_nh.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
mom_w_coriolis_nh.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
mom_w_coriolis_nh.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_w_coriolis_nh.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_w_coriolis_nh.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_w_coriolis_nh.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_w_coriolis_nh.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_w_coriolis_nh.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_w_coriolis_nh.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_w_coriolis_nh.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_w_coriolis_nh.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_w_coriolis_nh.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_w_metric_nh.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_w_metric_nh.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_w_metric_nh.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_w_metric_nh.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_w_metric_nh.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_w_metric_nh.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_w_metric_nh.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_w_metric_nh.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_w_metric_nh.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_w_metric_nh.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_w_metric_nh.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_w_metric_nh.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_w_sidedrag.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_w_sidedrag.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_w_sidedrag.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_w_sidedrag.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_w_sidedrag.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_w_sidedrag.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_w_sidedrag.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_w_sidedrag.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_w_sidedrag.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_w_sidedrag.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_w_sidedrag.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_w_sidedrag.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_w_sidedrag.for: SURFACE.h
mom_w_smag_3d.for: MOM_COMMON_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_w_smag_3d.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_w_smag_3d.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_w_smag_3d.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_w_smag_3d.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_w_smag_3d.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_w_smag_3d.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_w_smag_3d.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_w_smag_3d.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_w_smag_3d.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_w_smag_3d.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_w_smag_3d.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_calc_rtrans.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_calc_rtrans.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h DYNVARS.h
mom_calc_rtrans.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
mom_calc_rtrans.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
mom_calc_rtrans.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_calc_rtrans.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_calc_rtrans.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_calc_rtrans.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_calc_rtrans.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_calc_rtrans.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_calc_rtrans.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_calc_rtrans.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_calc_rtrans.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
mom_calc_rtrans.for: MOM_FLUXFORM.h
mom_fluxform.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_fluxform.for: CPP_EEOPTIONS.h CPP_EEMACROS.h MOM_COMMON_OPTIONS.h SIZE.h
mom_fluxform.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
mom_fluxform.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
mom_fluxform.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_fluxform.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_fluxform.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_fluxform.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_fluxform.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_fluxform.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_fluxform.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_fluxform.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_fluxform.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h FFIELDS.h
mom_fluxform.for: SURFACE.h MOM_VISC.h
mom_u_adv_uu.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_adv_uu.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_u_adv_uu.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_u_adv_uu.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
mom_u_adv_uu.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_u_adv_uu.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_u_adv_uu.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_u_adv_uu.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_u_adv_uu.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_u_adv_uu.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_u_adv_uu.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_u_adv_uu.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_u_adv_vu.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_adv_vu.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_u_adv_vu.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_u_adv_vu.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
mom_u_adv_vu.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_u_adv_vu.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_u_adv_vu.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_u_adv_vu.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_u_adv_vu.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_u_adv_vu.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_u_adv_vu.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_u_adv_vu.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_u_adv_wu.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_adv_wu.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_u_adv_wu.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_u_adv_wu.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
mom_u_adv_wu.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_u_adv_wu.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_u_adv_wu.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_u_adv_wu.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_u_adv_wu.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_u_adv_wu.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_u_adv_wu.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_u_adv_wu.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_u_coriolis.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_coriolis.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_u_coriolis.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_u_coriolis.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_u_coriolis.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_u_coriolis.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_u_coriolis.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_u_coriolis.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_u_coriolis.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_u_coriolis.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_u_coriolis.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_u_coriolis.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_u_coriolis.for: SURFACE.h
mom_u_del2u.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_del2u.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_u_del2u.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_u_del2u.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
mom_u_del2u.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_u_del2u.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_u_del2u.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_u_del2u.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_u_del2u.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_u_del2u.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_u_del2u.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_u_del2u.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
mom_u_metric_cylinder.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h
mom_u_metric_cylinder.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
mom_u_metric_cylinder.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h
mom_u_metric_cylinder.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_u_metric_cylinder.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_u_metric_cylinder.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_u_metric_cylinder.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_u_metric_cylinder.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_u_metric_cylinder.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_u_metric_cylinder.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_u_metric_cylinder.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_u_metric_cylinder.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
mom_u_metric_cylinder.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
mom_u_metric_cylinder.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_u_metric_cylinder.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
mom_u_metric_cylinder.for: FCORI_MACROS.h
mom_u_metric_sphere.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h
mom_u_metric_sphere.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
mom_u_metric_sphere.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h
mom_u_metric_sphere.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
mom_u_metric_sphere.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
mom_u_metric_sphere.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_u_metric_sphere.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_u_metric_sphere.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_u_metric_sphere.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_u_metric_sphere.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_u_metric_sphere.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_u_metric_sphere.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
mom_u_metric_sphere.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
mom_u_metric_sphere.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
mom_u_metric_sphere.for: FCORI_MACROS.h
mom_u_xviscflux.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_xviscflux.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_u_xviscflux.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_u_xviscflux.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_u_xviscflux.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_u_xviscflux.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_u_xviscflux.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_u_xviscflux.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_u_xviscflux.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_u_xviscflux.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_u_xviscflux.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_u_xviscflux.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_u_yviscflux.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_u_yviscflux.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_u_yviscflux.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_u_yviscflux.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_u_yviscflux.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_u_yviscflux.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_u_yviscflux.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_u_yviscflux.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_u_yviscflux.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_u_yviscflux.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_u_yviscflux.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_u_yviscflux.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_uv_boundary.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_uv_boundary.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_uv_boundary.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_uv_boundary.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_uv_boundary.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_uv_boundary.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_uv_boundary.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_uv_boundary.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_uv_boundary.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_uv_boundary.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_uv_boundary.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_uv_boundary.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_v_adv_uv.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_adv_uv.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_v_adv_uv.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_v_adv_uv.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
mom_v_adv_uv.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_v_adv_uv.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_v_adv_uv.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_v_adv_uv.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_v_adv_uv.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_v_adv_uv.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_v_adv_uv.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_v_adv_uv.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_v_adv_vv.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_adv_vv.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_v_adv_vv.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_v_adv_vv.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
mom_v_adv_vv.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_v_adv_vv.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_v_adv_vv.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_v_adv_vv.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_v_adv_vv.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_v_adv_vv.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_v_adv_vv.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_v_adv_vv.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_v_adv_wv.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_adv_wv.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_v_adv_wv.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_v_adv_wv.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
mom_v_adv_wv.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_v_adv_wv.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_v_adv_wv.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_v_adv_wv.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_v_adv_wv.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_v_adv_wv.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_v_adv_wv.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_v_adv_wv.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_v_coriolis.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_coriolis.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_v_coriolis.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_v_coriolis.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_v_coriolis.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_v_coriolis.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_v_coriolis.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_v_coriolis.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_v_coriolis.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_v_coriolis.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_v_coriolis.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_v_coriolis.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_v_coriolis.for: SURFACE.h
mom_v_del2v.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_del2v.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_v_del2v.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_v_del2v.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
mom_v_del2v.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_v_del2v.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_v_del2v.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_v_del2v.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_v_del2v.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_v_del2v.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_v_del2v.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_v_del2v.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
mom_v_metric_cylinder.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h
mom_v_metric_cylinder.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
mom_v_metric_cylinder.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h
mom_v_metric_cylinder.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_v_metric_cylinder.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_v_metric_cylinder.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_v_metric_cylinder.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_v_metric_cylinder.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_v_metric_cylinder.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_v_metric_cylinder.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_v_metric_cylinder.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_v_metric_cylinder.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
mom_v_metric_cylinder.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
mom_v_metric_cylinder.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_v_metric_cylinder.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
mom_v_metric_cylinder.for: FCORI_MACROS.h
mom_v_metric_sphere.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h
mom_v_metric_sphere.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
mom_v_metric_sphere.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h
mom_v_metric_sphere.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
mom_v_metric_sphere.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
mom_v_metric_sphere.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_v_metric_sphere.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_v_metric_sphere.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_v_metric_sphere.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_v_metric_sphere.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_v_metric_sphere.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_v_metric_sphere.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
mom_v_metric_sphere.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
mom_v_metric_sphere.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
mom_v_metric_sphere.for: FCORI_MACROS.h
mom_v_xviscflux.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_xviscflux.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_v_xviscflux.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_v_xviscflux.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_v_xviscflux.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_v_xviscflux.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_v_xviscflux.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_v_xviscflux.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_v_xviscflux.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_v_xviscflux.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_v_xviscflux.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_v_xviscflux.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_v_yviscflux.for: MOM_FLUXFORM_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_v_yviscflux.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_v_yviscflux.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_v_yviscflux.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_v_yviscflux.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_v_yviscflux.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_v_yviscflux.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_v_yviscflux.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_v_yviscflux.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_v_yviscflux.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_v_yviscflux.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_v_yviscflux.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_vecinv.for: MOM_VECINV_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_vecinv.for: CPP_EEOPTIONS.h CPP_EEMACROS.h MOM_COMMON_OPTIONS.h SIZE.h
mom_vecinv.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
mom_vecinv.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
mom_vecinv.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_vecinv.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_vecinv.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_vecinv.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_vecinv.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_vecinv.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_vecinv.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_vecinv.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_vecinv.for: SURFACE.h DYNVARS.h MOM_VISC.h TIMEAVE_STATV.h
mom_vecinv.for: TIMEAVE_OPTIONS.h
mom_vi_coriolis.for: MOM_VECINV_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_vi_coriolis.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h GRID.h
mom_vi_coriolis.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_vi_coriolis.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
mom_vi_coriolis.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_vi_coriolis.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_vi_coriolis.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_vi_coriolis.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_vi_coriolis.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_vi_coriolis.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_vi_coriolis.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_vi_coriolis.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_vi_coriolis.for: PARAMS.h
mom_vi_del2uv.for: MOM_VECINV_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_vi_del2uv.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h
mom_vi_del2uv.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
mom_vi_del2uv.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
mom_vi_del2uv.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_vi_del2uv.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_vi_del2uv.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_vi_del2uv.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_vi_del2uv.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_vi_del2uv.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_vi_del2uv.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_vi_del2uv.for: TANPHIATV_MACROS.h FCORI_MACROS.h EEPARAMS.h
mom_vi_hdissip.for: MOM_VECINV_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_vi_hdissip.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mom_vi_hdissip.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_vi_hdissip.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_vi_hdissip.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_vi_hdissip.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_vi_hdissip.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_vi_hdissip.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_vi_hdissip.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_vi_hdissip.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mom_vi_hdissip.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mom_vi_hdissip.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mom_vi_u_coriolis.for: MOM_VECINV_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_vi_u_coriolis.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_vi_u_coriolis.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_vi_u_coriolis.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_vi_u_coriolis.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_vi_u_coriolis.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_vi_u_coriolis.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_vi_u_coriolis.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_vi_u_coriolis.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_vi_u_coriolis.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_vi_u_coriolis.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_vi_u_coriolis.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_vi_u_coriolis.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_vi_u_coriolis.for: TANPHIATV_MACROS.h FCORI_MACROS.h PARAMS.h
mom_vi_u_coriolis_c4.for: MOM_VECINV_OPTIONS.h PACKAGES_CONFIG.h
mom_vi_u_coriolis_c4.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
mom_vi_u_coriolis_c4.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h
mom_vi_u_coriolis_c4.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
mom_vi_u_coriolis_c4.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
mom_vi_u_coriolis_c4.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_vi_u_coriolis_c4.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_vi_u_coriolis_c4.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_vi_u_coriolis_c4.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_vi_u_coriolis_c4.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_vi_u_coriolis_c4.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_vi_u_coriolis_c4.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
mom_vi_u_coriolis_c4.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_vi_u_coriolis_c4.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_vi_u_coriolis_c4.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_vi_u_grad_ke.for: MOM_VECINV_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_vi_u_grad_ke.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h GRID.h
mom_vi_u_grad_ke.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_vi_u_grad_ke.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
mom_vi_u_grad_ke.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_vi_u_grad_ke.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_vi_u_grad_ke.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_vi_u_grad_ke.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_vi_u_grad_ke.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_vi_u_grad_ke.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_vi_u_grad_ke.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
mom_vi_u_grad_ke.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
mom_vi_u_grad_ke.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
mom_vi_u_grad_ke.for: FCORI_MACROS.h
mom_vi_u_vertshear.for: MOM_VECINV_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_vi_u_vertshear.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_vi_u_vertshear.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_vi_u_vertshear.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_vi_u_vertshear.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_vi_u_vertshear.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_vi_u_vertshear.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_vi_u_vertshear.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_vi_u_vertshear.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_vi_u_vertshear.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_vi_u_vertshear.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_vi_u_vertshear.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_vi_u_vertshear.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_vi_u_vertshear.for: TANPHIATV_MACROS.h FCORI_MACROS.h PARAMS.h
mom_vi_v_coriolis.for: MOM_VECINV_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_vi_v_coriolis.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_vi_v_coriolis.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_vi_v_coriolis.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_vi_v_coriolis.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_vi_v_coriolis.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_vi_v_coriolis.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_vi_v_coriolis.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_vi_v_coriolis.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_vi_v_coriolis.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_vi_v_coriolis.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_vi_v_coriolis.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_vi_v_coriolis.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_vi_v_coriolis.for: TANPHIATV_MACROS.h FCORI_MACROS.h PARAMS.h
mom_vi_v_coriolis_c4.for: MOM_VECINV_OPTIONS.h PACKAGES_CONFIG.h
mom_vi_v_coriolis_c4.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
mom_vi_v_coriolis_c4.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h
mom_vi_v_coriolis_c4.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
mom_vi_v_coriolis_c4.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
mom_vi_v_coriolis_c4.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
mom_vi_v_coriolis_c4.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_vi_v_coriolis_c4.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_vi_v_coriolis_c4.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_vi_v_coriolis_c4.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_vi_v_coriolis_c4.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_vi_v_coriolis_c4.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
mom_vi_v_coriolis_c4.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_vi_v_coriolis_c4.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_vi_v_coriolis_c4.for: TANPHIATV_MACROS.h FCORI_MACROS.h
mom_vi_v_grad_ke.for: MOM_VECINV_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_vi_v_grad_ke.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h GRID.h
mom_vi_v_grad_ke.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mom_vi_v_grad_ke.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
mom_vi_v_grad_ke.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mom_vi_v_grad_ke.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mom_vi_v_grad_ke.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mom_vi_v_grad_ke.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
mom_vi_v_grad_ke.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mom_vi_v_grad_ke.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mom_vi_v_grad_ke.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
mom_vi_v_grad_ke.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
mom_vi_v_grad_ke.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
mom_vi_v_grad_ke.for: FCORI_MACROS.h
mom_vi_v_vertshear.for: MOM_VECINV_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mom_vi_v_vertshear.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mom_vi_v_vertshear.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mom_vi_v_vertshear.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mom_vi_v_vertshear.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mom_vi_v_vertshear.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mom_vi_v_vertshear.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
mom_vi_v_vertshear.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mom_vi_v_vertshear.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mom_vi_v_vertshear.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
mom_vi_v_vertshear.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
mom_vi_v_vertshear.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
mom_vi_v_vertshear.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
mom_vi_v_vertshear.for: TANPHIATV_MACROS.h FCORI_MACROS.h PARAMS.h
mon_advcfl.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_advcfl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h MONITOR.h
mon_advcflw.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_advcflw.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h MONITOR.h
mon_advcflw2.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_advcflw2.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h MONITOR.h
mon_calc_advcfl.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_calc_advcfl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mon_calc_advcfl.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mon_calc_advcfl.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mon_calc_advcfl.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mon_calc_advcfl.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mon_calc_advcfl.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mon_calc_advcfl.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mon_calc_advcfl.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mon_calc_advcfl.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mon_calc_advcfl.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mon_calc_advcfl.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mon_calc_advcfl.for: MONITOR.h
mon_calc_stats_rl.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_calc_stats_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mon_calc_stats_rs.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_calc_stats_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mon_init.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_init.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mon_init.for: MONITOR.h
mon_ke.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
mon_ke.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h DYNVARS.h MONITOR.h
mon_ke.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
mon_ke.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
mon_ke.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mon_ke.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mon_ke.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mon_ke.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mon_ke.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mon_ke.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mon_ke.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
mon_out.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_out.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mon_out.for: MONITOR.h
mon_printstats_rl.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_printstats_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mon_printstats_rl.for: MONITOR.h
mon_printstats_rs.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_printstats_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mon_printstats_rs.for: MONITOR.h
mon_set_iounit.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_set_iounit.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mon_set_iounit.for: MONITOR.h
mon_set_pref.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_set_pref.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h MONITOR.h
mon_solution.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_solution.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mon_solution.for: DYNVARS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
mon_solution.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
mon_solution.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
mon_solution.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
mon_solution.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
mon_solution.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
mon_solution.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mon_solution.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mon_solution.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mon_solution.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mon_solution.for: MONITOR.h
mon_stats_latbnd_rl.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_stats_latbnd_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mon_stats_rl.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_stats_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mon_stats_rs.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_stats_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mon_surfcor.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_surfcor.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mon_surfcor.for: DYNVARS.h SURFACE.h GRID.h GRID_MACROS.h DXC_MACROS.h
mon_surfcor.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
mon_surfcor.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mon_surfcor.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mon_surfcor.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mon_surfcor.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mon_surfcor.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mon_surfcor.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mon_surfcor.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mon_surfcor.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mon_surfcor.for: MONITOR.h
mon_vort3.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_vort3.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
mon_vort3.for: DYNVARS.h MONITOR.h GRID.h GRID_MACROS.h DXC_MACROS.h
mon_vort3.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
mon_vort3.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
mon_vort3.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
mon_vort3.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
mon_vort3.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
mon_vort3.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
mon_vort3.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
mon_vort3.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
mon_vort3.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
mon_writestats_rl.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_writestats_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mon_writestats_rl.for: MONITOR.h
mon_writestats_rs.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
mon_writestats_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mon_writestats_rs.for: MONITOR.h
monitor.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
monitor.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
monitor.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
monitor.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
monitor.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
monitor.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
monitor.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
monitor.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
monitor.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
monitor.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
monitor.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
monitor.for: FFIELDS.h MONITOR.h
monitor_ad.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
monitor_ad.for: CPP_EEOPTIONS.h CPP_EEMACROS.h AD_CONFIG.h SIZE.h EEPARAMS.h
monitor_ad.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
monitor_ad.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
monitor_ad.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
monitor_ad.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
monitor_ad.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
monitor_ad.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
monitor_ad.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
monitor_ad.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
monitor_ad.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
monitor_ad.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
monitor_ad.for: MONITOR.h
monitor_g.for: MONITOR_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
monitor_g.for: CPP_EEOPTIONS.h CPP_EEMACROS.h AD_CONFIG.h SIZE.h EEPARAMS.h
monitor_g.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
monitor_g.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
monitor_g.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
monitor_g.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
monitor_g.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
monitor_g.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
monitor_g.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
monitor_g.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
monitor_g.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
monitor_g.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h FFIELDS.h
monitor_g.for: MONITOR.h
obcs_add_tides.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_add_tides.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_add_tides.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
obcs_add_tides.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
obcs_add_tides.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
obcs_add_tides.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
obcs_add_tides.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_add_tides.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
obcs_add_tides.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
obcs_add_tides.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
obcs_add_tides.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
obcs_add_tides.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
obcs_add_tides.for: OBCS_PARAMS.h OBCS_GRID.h OBCS_FIELDS.h
obcs_adjust_uvice.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_adjust_uvice.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_adjust_uvice.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
obcs_adjust_uvice.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
obcs_adjust_uvice.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
obcs_adjust_uvice.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
obcs_adjust_uvice.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_adjust_uvice.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_adjust_uvice.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
obcs_adjust_uvice.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_adjust_uvice.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_adjust_uvice.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_adjust_uvice.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_adjust_uvice.for: TANPHIATV_MACROS.h FCORI_MACROS.h OBCS_PARAMS.h
obcs_adjust_uvice.for: OBCS_GRID.h OBCS_SEAICE.h
obcs_apply_eta.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_apply_eta.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_apply_eta.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
obcs_apply_eta.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
obcs_apply_eta.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
obcs_apply_eta.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
obcs_apply_eta.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_apply_eta.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
obcs_apply_eta.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
obcs_apply_eta.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
obcs_apply_eta.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
obcs_apply_eta.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
obcs_apply_eta.for: SURFACE.h OBCS_PARAMS.h OBCS_GRID.h OBCS_FIELDS.h
obcs_apply_ptracer.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_apply_ptracer.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_apply_ptracer.for: PARAMS.h OBCS_GRID.h
obcs_apply_r_star.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_apply_r_star.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_apply_r_star.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
obcs_apply_r_star.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
obcs_apply_r_star.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
obcs_apply_r_star.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
obcs_apply_r_star.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_apply_r_star.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_apply_r_star.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
obcs_apply_r_star.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_apply_r_star.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_apply_r_star.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_apply_r_star.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_apply_r_star.for: TANPHIATV_MACROS.h FCORI_MACROS.h OBCS_PARAMS.h
obcs_apply_r_star.for: OBCS_GRID.h OBCS_FIELDS.h
obcs_apply_seaice.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_apply_seaice.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_apply_seaice.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
obcs_apply_seaice.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
obcs_apply_seaice.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
obcs_apply_seaice.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
obcs_apply_seaice.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_apply_seaice.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_apply_seaice.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
obcs_apply_seaice.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_apply_seaice.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_apply_seaice.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_apply_seaice.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_apply_seaice.for: TANPHIATV_MACROS.h FCORI_MACROS.h OBCS_GRID.h
obcs_apply_seaice.for: OBCS_SEAICE.h
obcs_apply_surf_dr.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_apply_surf_dr.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_apply_surf_dr.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
obcs_apply_surf_dr.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
obcs_apply_surf_dr.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
obcs_apply_surf_dr.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
obcs_apply_surf_dr.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_apply_surf_dr.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_apply_surf_dr.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
obcs_apply_surf_dr.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_apply_surf_dr.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_apply_surf_dr.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_apply_surf_dr.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_apply_surf_dr.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
obcs_apply_surf_dr.for: OBCS_PARAMS.h OBCS_GRID.h OBCS_FIELDS.h
obcs_apply_ts.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_apply_ts.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_apply_ts.for: OBCS_PARAMS.h OBCS_GRID.h OBCS_FIELDS.h
obcs_apply_uv.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_apply_uv.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_apply_uv.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
obcs_apply_uv.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
obcs_apply_uv.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
obcs_apply_uv.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
obcs_apply_uv.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_apply_uv.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
obcs_apply_uv.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
obcs_apply_uv.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
obcs_apply_uv.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
obcs_apply_uv.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
obcs_apply_uv.for: OBCS_PARAMS.h OBCS_GRID.h OBCS_FIELDS.h
obcs_apply_uvice.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_apply_uvice.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_apply_uvice.for: PARAMS.h OBCS_PARAMS.h OBCS_GRID.h OBCS_SEAICE.h
obcs_apply_w.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_apply_w.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_apply_w.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
obcs_apply_w.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
obcs_apply_w.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
obcs_apply_w.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_apply_w.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
obcs_apply_w.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_apply_w.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_apply_w.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_apply_w.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_apply_w.for: TANPHIATV_MACROS.h FCORI_MACROS.h OBCS_PARAMS.h OBCS_GRID.h
obcs_apply_w.for: OBCS_FIELDS.h
obcs_balance_flow.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_balance_flow.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_balance_flow.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
obcs_balance_flow.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
obcs_balance_flow.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
obcs_balance_flow.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
obcs_balance_flow.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_balance_flow.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_balance_flow.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
obcs_balance_flow.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_balance_flow.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_balance_flow.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_balance_flow.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_balance_flow.for: TANPHIATV_MACROS.h FCORI_MACROS.h OBCS_PARAMS.h
obcs_balance_flow.for: OBCS_GRID.h OBCS_FIELDS.h
obcs_calc.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
obcs_calc.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h
obcs_calc.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
obcs_calc.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
obcs_calc.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
obcs_calc.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_calc.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
obcs_calc.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_calc.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_calc.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_calc.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_calc.for: TANPHIATV_MACROS.h FCORI_MACROS.h OBCS_PARAMS.h OBCS_GRID.h
obcs_calc.for: OBCS_FIELDS.h
obcs_calc_stevens.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_calc_stevens.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_calc_stevens.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
obcs_calc_stevens.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
obcs_calc_stevens.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
obcs_calc_stevens.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
obcs_calc_stevens.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_calc_stevens.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_calc_stevens.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
obcs_calc_stevens.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_calc_stevens.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_calc_stevens.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_calc_stevens.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_calc_stevens.for: TANPHIATV_MACROS.h FCORI_MACROS.h OBCS_PARAMS.h
obcs_calc_stevens.for: OBCS_GRID.h OBCS_FIELDS.h DYNVARS.h
obcs_check.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_check.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_check.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
obcs_check.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
obcs_check.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
obcs_check.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_check.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
obcs_check.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_check.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_check.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_check.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_check.for: TANPHIATV_MACROS.h FCORI_MACROS.h OBCS_PARAMS.h OBCS_GRID.h
obcs_check.for: OBCS_SEAICE.h
obcs_check_depths.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_check_depths.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_check_depths.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
obcs_check_depths.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
obcs_check_depths.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
obcs_check_depths.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
obcs_check_depths.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_check_depths.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_check_depths.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
obcs_check_depths.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_check_depths.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_check_depths.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_check_depths.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_check_depths.for: TANPHIATV_MACROS.h FCORI_MACROS.h OBCS_PARAMS.h
obcs_check_depths.for: OBCS_GRID.h
obcs_copy_tracer.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_copy_tracer.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_copy_tracer.for: PARAMS.h OBCS_GRID.h
obcs_copy_uv_n.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_copy_uv_n.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_copy_uv_n.for: OBCS_PARAMS.h OBCS_GRID.h
obcs_diag_balance.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_diag_balance.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_diag_balance.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
obcs_diag_balance.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
obcs_diag_balance.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
obcs_diag_balance.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
obcs_diag_balance.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_diag_balance.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_diag_balance.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
obcs_diag_balance.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_diag_balance.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_diag_balance.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_diag_balance.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_diag_balance.for: TANPHIATV_MACROS.h FCORI_MACROS.h OBCS_PARAMS.h
obcs_diag_balance.for: OBCS_GRID.h OBCS_FIELDS.h
obcs_exchanges.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_exchanges.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_exchanges.for: DYNVARS.h OBCS_PARAMS.h
obcs_exf_load.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_exf_load.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_exf_load.for: OBCS_PARAMS.h OBCS_FIELDS.h OBCS_SEAICE.h
obcs_fields_load.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_fields_load.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_fields_load.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
obcs_fields_load.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
obcs_fields_load.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
obcs_fields_load.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
obcs_fields_load.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
obcs_fields_load.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
obcs_fields_load.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
obcs_fields_load.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
obcs_fields_load.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
obcs_fields_load.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
obcs_fields_load.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
obcs_fields_load.for: FCORI_MACROS.h OBCS_PARAMS.h OBCS_FIELDS.h
obcs_init_fixed.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_init_fixed.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_init_fixed.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
obcs_init_fixed.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
obcs_init_fixed.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
obcs_init_fixed.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
obcs_init_fixed.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_init_fixed.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
obcs_init_fixed.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
obcs_init_fixed.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
obcs_init_fixed.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
obcs_init_fixed.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
obcs_init_fixed.for: OBCS_PARAMS.h OBCS_GRID.h
obcs_init_variables.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_init_variables.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_init_variables.for: PARAMS.h DYNVARS.h OBCS_PARAMS.h OBCS_FIELDS.h
obcs_init_variables.for: OBCS_SEAICE.h
obcs_mon_stats.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_mon_stats.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_monitor.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_monitor.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_monitor.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
obcs_monitor.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
obcs_monitor.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
obcs_monitor.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_monitor.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
obcs_monitor.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_monitor.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_monitor.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_monitor.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_monitor.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h OBCS_PARAMS.h
obcs_monitor.for: OBCS_GRID.h MONITOR.h
obcs_output.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_output.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_output.for: OBCS_PARAMS.h OBCS_FIELDS.h
obcs_prescribe_read.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_prescribe_read.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_prescribe_read.for: PARAMS.h
obcs_read_pickup.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_read_pickup.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_read_pickup.for: PARAMS.h OBCS_PARAMS.h OBCS_FIELDS.h ORLANSKI.h
obcs_readparms.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_readparms.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_readparms.for: OBCS_PARAMS.h OBCS_GRID.h OBCS_SEAICE.h ORLANSKI.h
obcs_save_uv_n.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_save_uv_n.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_save_uv_n.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
obcs_save_uv_n.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
obcs_save_uv_n.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
obcs_save_uv_n.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
obcs_save_uv_n.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_save_uv_n.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
obcs_save_uv_n.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
obcs_save_uv_n.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
obcs_save_uv_n.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
obcs_save_uv_n.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
obcs_save_uv_n.for: OBCS_PARAMS.h OBCS_GRID.h OBCS_FIELDS.h
obcs_seaice_sponge.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_seaice_sponge.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_seaice_sponge.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
obcs_seaice_sponge.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
obcs_seaice_sponge.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
obcs_seaice_sponge.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
obcs_seaice_sponge.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_seaice_sponge.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_seaice_sponge.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
obcs_seaice_sponge.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_seaice_sponge.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_seaice_sponge.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_seaice_sponge.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_seaice_sponge.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
obcs_seaice_sponge.for: OBCS_PARAMS.h OBCS_GRID.h OBCS_FIELDS.h OBCS_SEAICE.h
obcs_set_connect.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_set_connect.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_set_connect.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
obcs_set_connect.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
obcs_set_connect.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
obcs_set_connect.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
obcs_set_connect.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
obcs_set_connect.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
obcs_set_connect.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
obcs_set_connect.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
obcs_set_connect.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
obcs_set_connect.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
obcs_set_connect.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
obcs_set_connect.for: FCORI_MACROS.h OBCS_PARAMS.h OBCS_GRID.h
obcs_sponge.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_sponge.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
obcs_sponge.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
obcs_sponge.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
obcs_sponge.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
obcs_sponge.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_sponge.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
obcs_sponge.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_sponge.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_sponge.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_sponge.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_sponge.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h OBCS_PARAMS.h
obcs_sponge.for: OBCS_GRID.h OBCS_FIELDS.h
obcs_u1_adv_tracer.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_u1_adv_tracer.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_u1_adv_tracer.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
obcs_u1_adv_tracer.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
obcs_u1_adv_tracer.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
obcs_u1_adv_tracer.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
obcs_u1_adv_tracer.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
obcs_u1_adv_tracer.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
obcs_u1_adv_tracer.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
obcs_u1_adv_tracer.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
obcs_u1_adv_tracer.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
obcs_u1_adv_tracer.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
obcs_u1_adv_tracer.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
obcs_u1_adv_tracer.for: TANPHIATV_MACROS.h FCORI_MACROS.h OBCS_PARAMS.h GAD.h
obcs_write_pickup.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
obcs_write_pickup.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
obcs_write_pickup.for: PARAMS.h RESTART.h OBCS_PARAMS.h OBCS_FIELDS.h
obcs_write_pickup.for: ORLANSKI.h
orlanski_east.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
orlanski_east.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
orlanski_east.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
orlanski_east.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
orlanski_east.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
orlanski_east.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
orlanski_east.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
orlanski_east.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
orlanski_east.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
orlanski_east.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
orlanski_east.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
orlanski_east.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
orlanski_east.for: OBCS_PARAMS.h OBCS_GRID.h OBCS_FIELDS.h ORLANSKI.h
orlanski_init.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
orlanski_init.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
orlanski_init.for: ORLANSKI.h
orlanski_north.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
orlanski_north.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
orlanski_north.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
orlanski_north.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
orlanski_north.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
orlanski_north.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
orlanski_north.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
orlanski_north.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
orlanski_north.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
orlanski_north.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
orlanski_north.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
orlanski_north.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
orlanski_north.for: OBCS_PARAMS.h OBCS_GRID.h OBCS_FIELDS.h ORLANSKI.h
orlanski_south.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
orlanski_south.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
orlanski_south.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
orlanski_south.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
orlanski_south.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
orlanski_south.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
orlanski_south.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
orlanski_south.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
orlanski_south.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
orlanski_south.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
orlanski_south.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
orlanski_south.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
orlanski_south.for: OBCS_PARAMS.h OBCS_GRID.h OBCS_FIELDS.h ORLANSKI.h
orlanski_west.for: OBCS_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
orlanski_west.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
orlanski_west.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
orlanski_west.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
orlanski_west.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
orlanski_west.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
orlanski_west.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
orlanski_west.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
orlanski_west.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
orlanski_west.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
orlanski_west.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
orlanski_west.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
orlanski_west.for: OBCS_PARAMS.h OBCS_GRID.h OBCS_FIELDS.h ORLANSKI.h
get_write_global_fld.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
read_fld_xy_rl.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
read_fld_xy_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
read_fld_xy_rs.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
read_fld_xy_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
read_fld_xyz_rl.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
read_fld_xyz_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
read_fld_xyz_rl.for: PARAMS.h
read_fld_xyz_rs.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
read_fld_xyz_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
read_fld_xyz_rs.for: PARAMS.h
read_glvec_rl.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
read_glvec_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
read_glvec_rs.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
read_glvec_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
read_mflds.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
read_mflds.for: CPP_EEMACROS.h EEPARAMS.h RW_MFLDS.h SIZE.h PARAMS.h
read_rec.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
read_rec.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
set_write_global_fld.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
write_fld_3d_rl.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
write_fld_3d_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
write_fld_3d_rl.for: PARAMS.h
write_fld_3d_rs.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
write_fld_3d_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
write_fld_3d_rs.for: PARAMS.h
write_fld_s3d_rl.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
write_fld_s3d_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
write_fld_s3d_rl.for: PARAMS.h
write_fld_s3d_rs.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
write_fld_s3d_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
write_fld_s3d_rs.for: PARAMS.h
write_fld_xy_rl.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
write_fld_xy_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
write_fld_xy_rl.for: PARAMS.h
write_fld_xy_rs.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
write_fld_xy_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
write_fld_xy_rs.for: PARAMS.h
write_fld_xyz_rl.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
write_fld_xyz_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
write_fld_xyz_rl.for: PARAMS.h
write_fld_xyz_rs.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
write_fld_xyz_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
write_fld_xyz_rs.for: PARAMS.h
write_glvec_rl.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
write_glvec_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
write_glvec_rs.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
write_glvec_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
write_local_rl.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
write_local_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
write_local_rs.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
write_local_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
write_rec.for: RW_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
write_rec.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
timeave_cumul_1k1t.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timeave_cumul_1t.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timeave_cumul_1vfc.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timeave_cumul_2v.for: TIMEAVE_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
timeave_cumul_2v.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h GRID.h
timeave_cumul_2v.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
timeave_cumul_2v.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
timeave_cumul_2v.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
timeave_cumul_2v.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
timeave_cumul_2v.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
timeave_cumul_2v.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
timeave_cumul_2v.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
timeave_cumul_2v.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
timeave_cumul_2v.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
timeave_cumul_2v.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
timeave_cumul_2v.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
timeave_cumul_2v.for: FCORI_MACROS.h
timeave_cumul_2vfc.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timeave_cumul_dif_1t.for: TIMEAVE_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
timeave_cumul_dif_1t.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timeave_cumul_dif_1t.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
timeave_cumul_dif_1t.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
timeave_cumul_dif_1t.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
timeave_cumul_dif_1t.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
timeave_cumul_dif_1t.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
timeave_cumul_dif_1t.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
timeave_cumul_dif_1t.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
timeave_cumul_dif_1t.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
timeave_cumul_dif_1t.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
timeave_cumul_dif_1t.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
timeave_cumul_dif_1t.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
timeave_cumul_dif_1t.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
timeave_cumul_dif_1t.for: FCORI_MACROS.h
timeave_cumulate.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timeave_init_fixed.for: TIMEAVE_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
timeave_init_fixed.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timeave_init_fixed.for: PARAMS.h
timeave_norma_2v.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timeave_normalize.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timeave_reset.for: TIMEAVE_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
timeave_reset.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timeave_statv_write.for: TIMEAVE_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
timeave_statv_write.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timeave_statv_write.for: PARAMS.h DYNVARS.h GRID.h GRID_MACROS.h DXC_MACROS.h
timeave_statv_write.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
timeave_statv_write.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
timeave_statv_write.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
timeave_statv_write.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
timeave_statv_write.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
timeave_statv_write.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
timeave_statv_write.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
timeave_statv_write.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
timeave_statv_write.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
timeave_statv_write.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
timeave_statv_write.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
timeave_statv_write.for: FCORI_MACROS.h TIMEAVE_STATV.h
timeave_statvars.for: TIMEAVE_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
timeave_statvars.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timeave_statvars.for: PARAMS.h DYNVARS.h GRID.h GRID_MACROS.h DXC_MACROS.h
timeave_statvars.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
timeave_statvars.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
timeave_statvars.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
timeave_statvars.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
timeave_statvars.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
timeave_statvars.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
timeave_statvars.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
timeave_statvars.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
timeave_statvars.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
timeave_statvars.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
timeave_statvars.for: TANPHIATV_MACROS.h FCORI_MACROS.h TIMEAVE_STATV.h
timeave_surf_flux.for: TIMEAVE_OPTIONS.h PACKAGES_CONFIG.h CPP_OPTIONS.h
timeave_surf_flux.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timeave_surf_flux.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
timeave_surf_flux.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
timeave_surf_flux.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
timeave_surf_flux.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
timeave_surf_flux.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
timeave_surf_flux.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
timeave_surf_flux.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
timeave_surf_flux.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
timeave_surf_flux.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
timeave_surf_flux.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
timeave_surf_flux.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
timeave_surf_flux.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h SURFACE.h
timeave_surf_flux.for: FFIELDS.h TIMEAVE_STATV.h
all_proc_die.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
all_proc_die.for: EESUPPORT.h /usr/local/include/mpif.h
bar2.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
bar2.for: /usr/local/include/mpif.h BAR2.h
bar_check.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
barrier.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
barrier.for: /usr/local/include/mpif.h BARRIER.h
check_threads.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
check_threads.for: EESUPPORT.h /usr/local/include/mpif.h
comm_stats.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
comm_stats.for: /usr/local/include/mpif.h EXCH.h BAR2.h
cumulsum_z_tile.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
cumulsum_z_tile.for: EEPARAMS.h EESUPPORT.h /usr/local/include/mpif.h
cumulsum_z_tile.for: CUMULSUM.h
diff_phase_multiple.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
different_multiple.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
eeboot.for: CPP_EEOPTIONS.h CPP_EEMACROS.h PACKAGES_CONFIG.h SIZE.h
eeboot.for: EEPARAMS.h EESUPPORT.h /usr/local/include/mpif.h
eeboot_minimal.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
eeboot_minimal.for: EEPARAMS.h EESUPPORT.h /usr/local/include/mpif.h
eedata_example.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
eedie.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
eedie.for: /usr/local/include/mpif.h
eeintro_msg.for: CPP_EEOPTIONS.h CPP_EEMACROS.h BUILD_INFO.h SIZE.h
eeintro_msg.for: EEPARAMS.h EESUPPORT.h /usr/local/include/mpif.h
eeset_parms.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
eeset_parms.for: /usr/local/include/mpif.h EXCH.h
eewrite_eeenv.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
eewrite_eeenv.for: EESUPPORT.h /usr/local/include/mpif.h
exch0_r4.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch0_r8.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch0_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch0_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_bg_r4_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_bg_r8_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_bg_rl_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_bg_rs_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_r4.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EXCH.h
exch1_r4_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_r8.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EXCH.h
exch1_r8_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_rl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EXCH.h
exch1_rl_ad.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EXCH.h
exch1_rl_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_rl_cube_ad.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_rs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EXCH.h
exch1_rs_ad.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EXCH.h
exch1_rs_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_rs_cube_ad.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_uv_r4_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_uv_r8_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_uv_rl_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_uv_rs_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_z_r4_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_z_r8_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_z_rl_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch1_z_rs_cube.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_3d_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_3d_r4.for: EEPARAMS.h
exch_3d_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_3d_r8.for: EEPARAMS.h
exch_3d_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_3d_rl.for: EEPARAMS.h
exch_3d_rs.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_3d_rs.for: EEPARAMS.h
exch_cycle_ebl.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_cycle_ebl.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_init.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
exch_init.for: /usr/local/include/mpif.h EXCH.h
exch_r4_recv_get_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_r4_recv_get_x.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_r4_recv_get_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_r4_recv_get_y.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_r4_send_put_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_r4_send_put_x.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_r4_send_put_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_r4_send_put_y.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_r8_recv_get_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_r8_recv_get_x.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_r8_recv_get_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_r8_recv_get_y.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_r8_send_put_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_r8_send_put_x.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_r8_send_put_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_r8_send_put_y.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_rl_recv_get_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_rl_recv_get_x.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_rl_recv_get_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_rl_recv_get_y.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_rl_send_put_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_rl_send_put_x.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_rl_send_put_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_rl_send_put_y.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_rs_recv_get_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_rs_recv_get_x.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_rs_recv_get_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_rs_recv_get_y.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_rs_send_put_x.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_rs_send_put_x.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_rs_send_put_y.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
exch_rs_send_put_y.for: EESUPPORT.h /usr/local/include/mpif.h EXCH.h
exch_s3d_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_s3d_r4.for: EEPARAMS.h
exch_s3d_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_s3d_r8.for: EEPARAMS.h
exch_s3d_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_s3d_rl.for: EEPARAMS.h
exch_s3d_rs.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_s3d_rs.for: EEPARAMS.h
exch_sm_3d_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_sm_3d_r4.for: EEPARAMS.h
exch_sm_3d_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_sm_3d_r8.for: EEPARAMS.h
exch_sm_3d_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_sm_3d_rl.for: EEPARAMS.h
exch_sm_3d_rs.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_sm_3d_rs.for: EEPARAMS.h
exch_uv_3d_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_uv_3d_r4.for: EEPARAMS.h
exch_uv_3d_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_uv_3d_r8.for: EEPARAMS.h
exch_uv_3d_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_uv_3d_rl.for: EEPARAMS.h
exch_uv_3d_rs.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_uv_3d_rs.for: EEPARAMS.h
exch_uv_agrid_3d_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
exch_uv_agrid_3d_r4.for: SIZE.h EEPARAMS.h
exch_uv_agrid_3d_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
exch_uv_agrid_3d_r8.for: SIZE.h EEPARAMS.h
exch_uv_agrid_3d_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
exch_uv_agrid_3d_rl.for: SIZE.h EEPARAMS.h
exch_uv_agrid_3d_rs.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
exch_uv_agrid_3d_rs.for: SIZE.h EEPARAMS.h
exch_uv_bgrid_3d_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
exch_uv_bgrid_3d_r4.for: SIZE.h EEPARAMS.h
exch_uv_bgrid_3d_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
exch_uv_bgrid_3d_r8.for: SIZE.h EEPARAMS.h
exch_uv_bgrid_3d_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
exch_uv_bgrid_3d_rl.for: SIZE.h EEPARAMS.h
exch_uv_bgrid_3d_rs.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
exch_uv_bgrid_3d_rs.for: SIZE.h EEPARAMS.h
exch_uv_dgrid_3d_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
exch_uv_dgrid_3d_r4.for: SIZE.h EEPARAMS.h
exch_uv_dgrid_3d_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
exch_uv_dgrid_3d_r8.for: SIZE.h EEPARAMS.h
exch_uv_dgrid_3d_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
exch_uv_dgrid_3d_rl.for: SIZE.h EEPARAMS.h
exch_uv_dgrid_3d_rs.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
exch_uv_dgrid_3d_rs.for: SIZE.h EEPARAMS.h
exch_uv_xy_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_uv_xy_r4.for: EEPARAMS.h
exch_uv_xy_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_uv_xy_r8.for: EEPARAMS.h
exch_uv_xy_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_uv_xy_rl.for: EEPARAMS.h
exch_uv_xy_rs.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_uv_xy_rs.for: EEPARAMS.h
exch_uv_xyz_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_uv_xyz_r4.for: EEPARAMS.h
exch_uv_xyz_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_uv_xyz_r8.for: EEPARAMS.h
exch_uv_xyz_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_uv_xyz_rl.for: EEPARAMS.h
exch_uv_xyz_rs.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_uv_xyz_rs.for: EEPARAMS.h
exch_xy_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_xy_r4.for: EEPARAMS.h
exch_xy_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_xy_r8.for: EEPARAMS.h
exch_xy_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_xy_rl.for: EEPARAMS.h
exch_xy_rs.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_xy_rs.for: EEPARAMS.h
exch_xyz_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_xyz_r4.for: EEPARAMS.h
exch_xyz_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_xyz_r8.for: EEPARAMS.h
exch_xyz_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_xyz_rl.for: EEPARAMS.h
exch_xyz_rs.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_xyz_rs.for: EEPARAMS.h
exch_z_3d_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_z_3d_r4.for: EEPARAMS.h
exch_z_3d_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_z_3d_r8.for: EEPARAMS.h
exch_z_3d_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_z_3d_rl.for: EEPARAMS.h
exch_z_3d_rs.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
exch_z_3d_rs.for: EEPARAMS.h
fill_cs_corner_ag_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
fill_cs_corner_ag_rl.for: SIZE.h EEPARAMS.h
fill_cs_corner_tr_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
fill_cs_corner_tr_rl.for: SIZE.h EEPARAMS.h
fill_cs_corner_uv_rl.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
fill_cs_corner_uv_rl.for: SIZE.h EEPARAMS.h
fill_cs_corner_uv_rs.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
fill_cs_corner_uv_rs.for: SIZE.h EEPARAMS.h
fool_the_compiler.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
gather_2d_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
gather_2d_r4.for: EEPARAMS.h EESUPPORT.h /usr/local/include/mpif.h
gather_2d_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
gather_2d_r8.for: EEPARAMS.h EESUPPORT.h /usr/local/include/mpif.h
gather_2d_wh_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
gather_2d_wh_r4.for: EEPARAMS.h EESUPPORT.h /usr/local/include/mpif.h
gather_2d_wh_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
gather_2d_wh_r8.for: EEPARAMS.h EESUPPORT.h /usr/local/include/mpif.h
gather_vec_r4.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
gather_vec_r4.for: EESUPPORT.h /usr/local/include/mpif.h
gather_vec_r8.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
gather_vec_r8.for: EESUPPORT.h /usr/local/include/mpif.h
gather_xz.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
gather_xz.for: EESUPPORT.h /usr/local/include/mpif.h
gather_yz.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
gather_yz.for: EESUPPORT.h /usr/local/include/mpif.h
get_periodic_interval.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h
global_max.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
global_max.for: /usr/local/include/mpif.h GLOBAL_MAX.h
global_sum.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
global_sum.for: /usr/local/include/mpif.h GLOBAL_SUM.h
global_sum_singlecpu.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h
global_sum_singlecpu.for: SIZE.h EEPARAMS.h EESUPPORT.h
global_sum_singlecpu.for: /usr/local/include/mpif.h GLOBAL_SUM.h
global_sum_singlecpu.for: EEBUFF_SCPU.h
global_sum_tile.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
global_sum_tile.for: EESUPPORT.h /usr/local/include/mpif.h GLOBAL_SUM.h
global_vec_sum.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
global_vec_sum.for: EESUPPORT.h /usr/local/include/mpif.h
gsum.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
gsum.for: /usr/local/include/mpif.h
ini_communication_patterns.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h
ini_communication_patterns.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
ini_communication_patterns.for: /usr/local/include/mpif.h EXCH.h
ini_procs.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
ini_procs.for: /usr/local/include/mpif.h
ini_threading_environment.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
ini_threading_environment.for: PACKAGES_CONFIG.h SIZE.h EEPARAMS.h
ini_threading_environment.for: EESUPPORT.h /usr/local/include/mpif.h
lef_zero.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
main.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
main.for: SIZE.h EEPARAMS.h EESUPPORT.h /usr/local/include/mpif.h PARAMS.h
main.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
main.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
main.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
main.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
main.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
main.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
main.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
main.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
main.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
main.for: FFIELDS.h SURFACE.h MAIN_PDIRECTIVES1.h MAIN_PDIRECTIVES2.h
master_cpu_io.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
master_cpu_thread.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
master_cpu_thread.for: EESUPPORT.h /usr/local/include/mpif.h
mds_byteswapi4.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
mds_byteswapr4.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
mds_byteswapr8.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
mds_flush.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h
mds_reclen.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
mdsfindunit.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h
memsync.for: CPP_EEOPTIONS.h CPP_EEMACROS.h
nml_change_syntax.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h
nml_set_terminator.for: CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h
open_copy_data_file.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
print.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
print.for: /usr/local/include/mpif.h
reset_halo.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
scatter_2d_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
scatter_2d_r4.for: EEPARAMS.h EESUPPORT.h /usr/local/include/mpif.h
scatter_2d_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
scatter_2d_r8.for: EEPARAMS.h EESUPPORT.h /usr/local/include/mpif.h
scatter_2d_wh_r4.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
scatter_2d_wh_r4.for: EEPARAMS.h EESUPPORT.h /usr/local/include/mpif.h
scatter_2d_wh_r8.for: PACKAGES_CONFIG.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
scatter_2d_wh_r8.for: EEPARAMS.h EESUPPORT.h /usr/local/include/mpif.h
scatter_vec_r4.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
scatter_vec_r4.for: EESUPPORT.h /usr/local/include/mpif.h
scatter_vec_r8.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
scatter_vec_r8.for: EESUPPORT.h /usr/local/include/mpif.h
scatter_xz.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
scatter_xz.for: /usr/local/include/mpif.h
scatter_yz.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
scatter_yz.for: /usr/local/include/mpif.h
stop_if_error.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
timers.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
timers.for: /usr/local/include/mpif.h
utils.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
write_utils.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
adams_bashforth2.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
adams_bashforth2.for: EEPARAMS.h PARAMS.h
adams_bashforth3.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
adams_bashforth3.for: EEPARAMS.h PARAMS.h
add_walls2masks.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
add_walls2masks.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
add_walls2masks.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
add_walls2masks.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
add_walls2masks.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
add_walls2masks.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
add_walls2masks.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
add_walls2masks.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
add_walls2masks.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
add_walls2masks.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
add_walls2masks.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
add_walls2masks.for: TANPHIATV_MACROS.h FCORI_MACROS.h
apply_forcing.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
apply_forcing.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
apply_forcing.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
apply_forcing.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
apply_forcing.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
apply_forcing.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
apply_forcing.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
apply_forcing.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
apply_forcing.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
apply_forcing.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
apply_forcing.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
apply_forcing.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h FFIELDS.h
apply_forcing.for: SURFACE.h
calc_3d_diffusivity.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
calc_3d_diffusivity.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h DYNVARS.h
calc_3d_diffusivity.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
calc_3d_diffusivity.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
calc_3d_diffusivity.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
calc_3d_diffusivity.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
calc_3d_diffusivity.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
calc_3d_diffusivity.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
calc_3d_diffusivity.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
calc_3d_diffusivity.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
calc_3d_diffusivity.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
calc_3d_diffusivity.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
calc_3d_diffusivity.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
calc_3d_diffusivity.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
calc_3d_diffusivity.for: GAD.h
calc_adv_flow.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
calc_adv_flow.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
calc_adv_flow.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
calc_adv_flow.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
calc_adv_flow.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
calc_adv_flow.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
calc_adv_flow.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
calc_adv_flow.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
calc_adv_flow.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
calc_adv_flow.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
calc_adv_flow.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
calc_adv_flow.for: TANPHIATV_MACROS.h FCORI_MACROS.h
calc_div_ghat.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
calc_div_ghat.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
calc_div_ghat.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
calc_div_ghat.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
calc_div_ghat.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
calc_div_ghat.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
calc_div_ghat.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
calc_div_ghat.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
calc_div_ghat.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
calc_div_ghat.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
calc_div_ghat.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
calc_div_ghat.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
calc_eddy_stress.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
calc_eddy_stress.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
calc_eddy_stress.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
calc_eddy_stress.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
calc_eddy_stress.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
calc_eddy_stress.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
calc_eddy_stress.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
calc_eddy_stress.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
calc_eddy_stress.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
calc_eddy_stress.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
calc_eddy_stress.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
calc_eddy_stress.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
calc_eddy_stress.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
calc_eddy_stress.for: FCORI_MACROS.h FFIELDS.h
calc_grad_phi_fv.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
calc_grad_phi_fv.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
calc_grad_phi_fv.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
calc_grad_phi_fv.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
calc_grad_phi_fv.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
calc_grad_phi_fv.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
calc_grad_phi_fv.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
calc_grad_phi_fv.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
calc_grad_phi_fv.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
calc_grad_phi_fv.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
calc_grad_phi_fv.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
calc_grad_phi_fv.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
calc_grad_phi_fv.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
calc_grad_phi_hyd.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
calc_grad_phi_hyd.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
calc_grad_phi_hyd.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
calc_grad_phi_hyd.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
calc_grad_phi_hyd.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
calc_grad_phi_hyd.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
calc_grad_phi_hyd.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
calc_grad_phi_hyd.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
calc_grad_phi_hyd.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
calc_grad_phi_hyd.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
calc_grad_phi_hyd.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
calc_grad_phi_hyd.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
calc_grad_phi_hyd.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h DYNVARS.h
calc_grad_phi_surf.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
calc_grad_phi_surf.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
calc_grad_phi_surf.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
calc_grad_phi_surf.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
calc_grad_phi_surf.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
calc_grad_phi_surf.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
calc_grad_phi_surf.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
calc_grad_phi_surf.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
calc_grad_phi_surf.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
calc_grad_phi_surf.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
calc_grad_phi_surf.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
calc_grad_phi_surf.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
calc_grad_phi_surf.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
calc_grid_angles.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
calc_grid_angles.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
calc_grid_angles.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
calc_grid_angles.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
calc_grid_angles.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
calc_grid_angles.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
calc_grid_angles.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
calc_grid_angles.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
calc_grid_angles.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
calc_grid_angles.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
calc_grid_angles.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
calc_grid_angles.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
calc_grid_angles.for: TANPHIATV_MACROS.h FCORI_MACROS.h
calc_gw.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
calc_gw.for: MOM_COMMON_OPTIONS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
calc_gw.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
calc_gw.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
calc_gw.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
calc_gw.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
calc_gw.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
calc_gw.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
calc_gw.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
calc_gw.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
calc_gw.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h RESTART.h
calc_gw.for: SURFACE.h DYNVARS.h NH_VARS.h MOM_VISC.h
calc_ivdc.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
calc_ivdc.for: PARAMS.h DYNVARS.h GRID.h GRID_MACROS.h DXC_MACROS.h
calc_ivdc.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
calc_ivdc.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
calc_ivdc.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
calc_ivdc.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
calc_ivdc.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
calc_ivdc.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
calc_ivdc.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
calc_ivdc.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
calc_ivdc.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
calc_oce_mxlayer.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
calc_oce_mxlayer.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
calc_oce_mxlayer.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
calc_oce_mxlayer.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
calc_oce_mxlayer.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
calc_oce_mxlayer.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
calc_oce_mxlayer.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
calc_oce_mxlayer.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
calc_oce_mxlayer.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
calc_oce_mxlayer.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
calc_oce_mxlayer.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
calc_oce_mxlayer.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
calc_oce_mxlayer.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
calc_oce_mxlayer.for: FCORI_MACROS.h DYNVARS.h
calc_phi_hyd.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
calc_phi_hyd.for: CPP_EEMACROS.h SIZE.h GRID.h GRID_MACROS.h DXC_MACROS.h
calc_phi_hyd.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
calc_phi_hyd.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
calc_phi_hyd.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
calc_phi_hyd.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
calc_phi_hyd.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
calc_phi_hyd.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
calc_phi_hyd.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
calc_phi_hyd.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
calc_phi_hyd.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
calc_phi_hyd.for: TANPHIATV_MACROS.h FCORI_MACROS.h EEPARAMS.h PARAMS.h
calc_phi_hyd.for: SURFACE.h DYNVARS.h
calc_r_star.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
calc_r_star.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
calc_r_star.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
calc_r_star.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
calc_r_star.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
calc_r_star.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
calc_r_star.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
calc_r_star.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
calc_r_star.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
calc_r_star.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
calc_r_star.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
calc_r_star.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
calc_surf_dr.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
calc_surf_dr.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
calc_surf_dr.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
calc_surf_dr.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
calc_surf_dr.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
calc_surf_dr.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
calc_surf_dr.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
calc_surf_dr.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
calc_surf_dr.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
calc_surf_dr.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
calc_surf_dr.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
calc_surf_dr.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
calc_viscosity.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
calc_viscosity.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h DYNVARS.h
calc_viscosity.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
calc_viscosity.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
calc_viscosity.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
calc_viscosity.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
calc_viscosity.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
calc_viscosity.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
calc_viscosity.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
calc_viscosity.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
calc_viscosity.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
calc_viscosity.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
calc_wsurf_tr.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
calc_wsurf_tr.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
calc_wsurf_tr.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
calc_wsurf_tr.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
calc_wsurf_tr.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
calc_wsurf_tr.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
calc_wsurf_tr.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
calc_wsurf_tr.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
calc_wsurf_tr.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
calc_wsurf_tr.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
calc_wsurf_tr.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
calc_wsurf_tr.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
cg2d.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
cg2d.for: PARAMS.h CG2D.h
cg2d_ex0.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
cg2d_ex0.for: PARAMS.h CG2D.h
cg2d_nsa.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
cg2d_nsa.for: SIZE.h EEPARAMS.h PARAMS.h CG2D.h
cg2d_sr.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
cg2d_sr.for: PARAMS.h CG2D.h
cg3d.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
cg3d.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
cg3d.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
cg3d.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
cg3d.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
cg3d.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
cg3d.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
cg3d.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
cg3d.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
cg3d.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
cg3d.for: CG3D.h
cg3d_ex0.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
cg3d_ex0.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
cg3d_ex0.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
cg3d_ex0.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
cg3d_ex0.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
cg3d_ex0.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
cg3d_ex0.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
cg3d_ex0.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
cg3d_ex0.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
cg3d_ex0.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
cg3d_ex0.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h CG3D.h
check_pickup.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
check_pickup.for: EEPARAMS.h PARAMS.h RESTART.h
config_check.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
config_check.for: CPP_EEMACROS.h MOM_COMMON_OPTIONS.h SIZE.h EEPARAMS.h
config_check.for: PARAMS.h
config_summary.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
config_summary.for: CPP_EEMACROS.h MOM_COMMON_OPTIONS.h SIZE.h EEPARAMS.h
config_summary.for: PARAMS.h EOS.h GRID.h GRID_MACROS.h DXC_MACROS.h
config_summary.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
config_summary.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
config_summary.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
config_summary.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
config_summary.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
config_summary.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
config_summary.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
config_summary.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
config_summary.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
config_summary.for: TANPHIATV_MACROS.h FCORI_MACROS.h MOM_VISC.h SET_GRID.h
convective_adjustment.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
convective_adjustment.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
convective_adjustment.for: DYNVARS.h GRID.h GRID_MACROS.h DXC_MACROS.h
convective_adjustment.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
convective_adjustment.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
convective_adjustment.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
convective_adjustment.for: HFACW_MACROS.h RECIP_DXC_MACROS.h
convective_adjustment.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
convective_adjustment.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
convective_adjustment.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
convective_adjustment.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
convective_adjustment.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
convective_adjustment.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
convective_adjustment.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
convective_adjustment.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
convective_adjustment.for: FCORI_MACROS.h TIMEAVE_STATV.h TIMEAVE_OPTIONS.h
convective_adjustment_ini.for: PACKAGES_CONFIG.h CPP_OPTIONS.h
convective_adjustment_ini.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
convective_adjustment_ini.for: EEPARAMS.h PARAMS.h DYNVARS.h GRID.h
convective_adjustment_ini.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
convective_adjustment_ini.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
convective_adjustment_ini.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
convective_adjustment_ini.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
convective_adjustment_ini.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
convective_adjustment_ini.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
convective_adjustment_ini.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
convective_adjustment_ini.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
convective_adjustment_ini.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
convective_adjustment_ini.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
convective_adjustment_ini.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
convective_adjustment_ini.for: MASKW_MACROS.h MASKS_MACROS.h
convective_adjustment_ini.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
convective_adjustment_ini.for: FCORI_MACROS.h TIMEAVE_STATV.h
convective_adjustment_ini.for: TIMEAVE_OPTIONS.h
convective_weights.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
convective_weights.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
convective_weights.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
convective_weights.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
convective_weights.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
convective_weights.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
convective_weights.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
convective_weights.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
convective_weights.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
convective_weights.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
convective_weights.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
convective_weights.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
convective_weights.for: TANPHIATV_MACROS.h FCORI_MACROS.h
convectively_mixtracer.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
convectively_mixtracer.for: SIZE.h EEPARAMS.h
correction_step.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
correction_step.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
correction_step.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
correction_step.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
correction_step.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
correction_step.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
correction_step.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
correction_step.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
correction_step.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
correction_step.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
correction_step.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
correction_step.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
correction_step.for: DYNVARS.h
cycle_ab_tracer.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
cycle_ab_tracer.for: EEPARAMS.h PARAMS.h
cycle_tracer.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
cycle_tracer.for: EEPARAMS.h PARAMS.h
diags_oceanic_surf_flux.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
diags_oceanic_surf_flux.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
diags_oceanic_surf_flux.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
diags_oceanic_surf_flux.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
diags_oceanic_surf_flux.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
diags_oceanic_surf_flux.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
diags_oceanic_surf_flux.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
diags_oceanic_surf_flux.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
diags_oceanic_surf_flux.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
diags_oceanic_surf_flux.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
diags_oceanic_surf_flux.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
diags_oceanic_surf_flux.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
diags_oceanic_surf_flux.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
diags_oceanic_surf_flux.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
diags_oceanic_surf_flux.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
diags_oceanic_surf_flux.for: SURFACE.h FFIELDS.h
diags_phi_hyd.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
diags_phi_hyd.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
diags_phi_hyd.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
diags_phi_hyd.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
diags_phi_hyd.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
diags_phi_hyd.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
diags_phi_hyd.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
diags_phi_hyd.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
diags_phi_hyd.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
diags_phi_hyd.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
diags_phi_hyd.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
diags_phi_hyd.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h DYNVARS.h
diags_phi_rlow.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
diags_phi_rlow.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
diags_phi_rlow.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
diags_phi_rlow.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
diags_phi_rlow.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
diags_phi_rlow.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
diags_phi_rlow.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
diags_phi_rlow.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
diags_phi_rlow.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
diags_phi_rlow.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
diags_phi_rlow.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
diags_phi_rlow.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h DYNVARS.h
diags_rho.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
diags_rho.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
diags_rho.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
diags_rho.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
diags_rho.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
diags_rho.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
diags_rho.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
diags_rho.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
diags_rho.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
diags_rho.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
diags_rho.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
do_atmospheric_phys.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
do_atmospheric_phys.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
do_atmospheric_phys.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
do_atmospheric_phys.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
do_atmospheric_phys.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
do_atmospheric_phys.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
do_atmospheric_phys.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
do_atmospheric_phys.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
do_atmospheric_phys.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
do_atmospheric_phys.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
do_atmospheric_phys.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
do_atmospheric_phys.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
do_atmospheric_phys.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
do_atmospheric_phys.for: FCORI_MACROS.h DYNVARS.h
do_fields_blocking_exchanges.for: PACKAGES_CONFIG.h CPP_OPTIONS.h
do_fields_blocking_exchanges.for: CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
do_fields_blocking_exchanges.for: EEPARAMS.h PARAMS.h DYNVARS.h GAD.h
do_oceanic_phys.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
do_oceanic_phys.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
do_oceanic_phys.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
do_oceanic_phys.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
do_oceanic_phys.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
do_oceanic_phys.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
do_oceanic_phys.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
do_oceanic_phys.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
do_oceanic_phys.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
do_oceanic_phys.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
do_oceanic_phys.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
do_oceanic_phys.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
do_oceanic_phys.for: DYNVARS.h TIMEAVE_STATV.h TIMEAVE_OPTIONS.h
do_stagger_fields_exchanges.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
do_stagger_fields_exchanges.for: SIZE.h EEPARAMS.h PARAMS.h DYNVARS.h
do_statevars_diags.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
do_statevars_diags.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
do_statevars_tave.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
do_statevars_tave.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
do_the_model_io.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
do_the_model_io.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h DYNVARS.h
do_write_pickup.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
do_write_pickup.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h RESTART.h
dynamics.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
dynamics.for: MOM_COMMON_OPTIONS.h OBCS_OPTIONS.h SIZE.h EEPARAMS.h PARAMS.h
dynamics.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
dynamics.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
dynamics.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
dynamics.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
dynamics.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
dynamics.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
dynamics.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
dynamics.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
dynamics.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
dynamics.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h MOM_VISC.h
external_fields_load.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
external_fields_load.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h FFIELDS.h
external_fields_load.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
external_fields_load.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
external_fields_load.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
external_fields_load.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
external_fields_load.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
external_fields_load.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
external_fields_load.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
external_fields_load.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
external_fields_load.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
external_fields_load.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
external_fields_load.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
external_fields_load.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
external_fields_load.for: FCORI_MACROS.h DYNVARS.h
external_forcing.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
external_forcing.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
external_forcing.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
external_forcing.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
external_forcing.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
external_forcing.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
external_forcing.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
external_forcing.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
external_forcing.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
external_forcing.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
external_forcing.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
external_forcing.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
external_forcing.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
external_forcing.for: FCORI_MACROS.h DYNVARS.h FFIELDS.h SURFACE.h
external_forcing_surf.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
external_forcing_surf.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
external_forcing_surf.for: FFIELDS.h DYNVARS.h GRID.h GRID_MACROS.h
external_forcing_surf.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
external_forcing_surf.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
external_forcing_surf.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
external_forcing_surf.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
external_forcing_surf.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
external_forcing_surf.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
external_forcing_surf.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
external_forcing_surf.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
external_forcing_surf.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
external_forcing_surf.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
external_forcing_surf.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
external_forcing_surf.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
external_forcing_surf.for: FCORI_MACROS.h SURFACE.h
find_alpha.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
find_alpha.for: CPP_EEMACROS.h SIZE.h DYNVARS.h EEPARAMS.h PARAMS.h EOS.h
find_alpha.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
find_alpha.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
find_alpha.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
find_alpha.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
find_alpha.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
find_alpha.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
find_alpha.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
find_alpha.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
find_alpha.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
find_alpha.for: TANPHIATV_MACROS.h FCORI_MACROS.h
find_hyd_press_1d.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
find_hyd_press_1d.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
find_hyd_press_1d.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
find_hyd_press_1d.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
find_hyd_press_1d.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
find_hyd_press_1d.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
find_hyd_press_1d.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
find_hyd_press_1d.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
find_hyd_press_1d.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
find_hyd_press_1d.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
find_hyd_press_1d.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
find_hyd_press_1d.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
find_hyd_press_1d.for: TANPHIATV_MACROS.h FCORI_MACROS.h
find_rho.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
find_rho.for: SIZE.h EEPARAMS.h PARAMS.h EOS.h
forcing_surf_relax.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
forcing_surf_relax.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h FFIELDS.h
forcing_surf_relax.for: DYNVARS.h GRID.h GRID_MACROS.h DXC_MACROS.h
forcing_surf_relax.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
forcing_surf_relax.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
forcing_surf_relax.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
forcing_surf_relax.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
forcing_surf_relax.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
forcing_surf_relax.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
forcing_surf_relax.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
forcing_surf_relax.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
forcing_surf_relax.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
forcing_surf_relax.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
forcing_surf_relax.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
forward_step.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
forward_step.for: CPP_EEMACROS.h GAD_OPTIONS.h OBCS_OPTIONS.h SIZE.h
forward_step.for: EEPARAMS.h PARAMS.h DYNVARS.h
freesurf_rescale_g.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
freesurf_rescale_g.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
freesurf_rescale_g.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
freesurf_rescale_g.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
freesurf_rescale_g.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
freesurf_rescale_g.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
freesurf_rescale_g.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
freesurf_rescale_g.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
freesurf_rescale_g.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
freesurf_rescale_g.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
freesurf_rescale_g.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
freesurf_rescale_g.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
freesurf_rescale_g.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
freeze_surface.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
freeze_surface.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h DYNVARS.h
freeze_surface.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
freeze_surface.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
freeze_surface.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
freeze_surface.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
freeze_surface.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
freeze_surface.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
freeze_surface.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
freeze_surface.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
freeze_surface.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
freeze_surface.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
freeze_surface.for: FFIELDS.h
grad_sigma.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
grad_sigma.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
grad_sigma.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
grad_sigma.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
grad_sigma.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
grad_sigma.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
grad_sigma.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
grad_sigma.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
grad_sigma.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
grad_sigma.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
grad_sigma.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
gsw_teos10.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
impldiff.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
impldiff.for: SIZE.h DYNVARS.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h
impldiff.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
impldiff.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
impldiff.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
impldiff.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
impldiff.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
impldiff.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
impldiff.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
impldiff.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
impldiff.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h GAD.h
ini_cartesian_grid.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
ini_cartesian_grid.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
ini_cartesian_grid.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
ini_cartesian_grid.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_cartesian_grid.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
ini_cartesian_grid.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_cartesian_grid.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
ini_cartesian_grid.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
ini_cartesian_grid.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_cartesian_grid.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_cartesian_grid.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_cartesian_grid.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_cartesian_grid.for: TANPHIATV_MACROS.h FCORI_MACROS.h
ini_cg2d.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
ini_cg2d.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
ini_cg2d.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
ini_cg2d.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_cg2d.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
ini_cg2d.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
ini_cg2d.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
ini_cg2d.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
ini_cg2d.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
ini_cg2d.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
ini_cg2d.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
ini_cg2d.for: CG2D.h
ini_cg3d.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
ini_cg3d.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
ini_cg3d.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
ini_cg3d.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_cg3d.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
ini_cg3d.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
ini_cg3d.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
ini_cg3d.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
ini_cg3d.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
ini_cg3d.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
ini_cg3d.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
ini_cg3d.for: CG3D.h SOLVE_FOR_PRESSURE3D.h
ini_cori.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
ini_cori.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
ini_cori.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
ini_cori.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_cori.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
ini_cori.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
ini_cori.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
ini_cori.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
ini_cori.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
ini_cori.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
ini_cori.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h MONITOR.h
ini_curvilinear_grid.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
ini_curvilinear_grid.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
ini_curvilinear_grid.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
ini_curvilinear_grid.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
ini_curvilinear_grid.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_curvilinear_grid.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
ini_curvilinear_grid.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_curvilinear_grid.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
ini_curvilinear_grid.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
ini_curvilinear_grid.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_curvilinear_grid.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
ini_curvilinear_grid.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
ini_curvilinear_grid.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
ini_curvilinear_grid.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
ini_curvilinear_grid.for: FCORI_MACROS.h
ini_cylinder_grid.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
ini_cylinder_grid.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
ini_cylinder_grid.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
ini_cylinder_grid.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_cylinder_grid.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
ini_cylinder_grid.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_cylinder_grid.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
ini_cylinder_grid.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
ini_cylinder_grid.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_cylinder_grid.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_cylinder_grid.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_cylinder_grid.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_cylinder_grid.for: TANPHIATV_MACROS.h FCORI_MACROS.h
ini_depths.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
ini_depths.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
ini_depths.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
ini_depths.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
ini_depths.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
ini_depths.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_depths.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_depths.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_depths.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_depths.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_depths.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_depths.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
ini_dynvars.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
ini_dynvars.for: EEPARAMS.h PARAMS.h DYNVARS.h
ini_eos.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
ini_eos.for: PARAMS.h EOS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
ini_eos.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
ini_eos.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
ini_eos.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_eos.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_eos.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_eos.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_eos.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
ini_eos.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
ini_eos.for: FCORI_MACROS.h DYNVARS.h
ini_ffields.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
ini_ffields.for: EEPARAMS.h PARAMS.h FFIELDS.h
ini_fields.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
ini_fields.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
ini_forcing.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
ini_forcing.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
ini_forcing.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
ini_forcing.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
ini_forcing.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
ini_forcing.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_forcing.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_forcing.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_forcing.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_forcing.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_forcing.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_forcing.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h FFIELDS.h
ini_global_domain.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
ini_global_domain.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
ini_global_domain.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
ini_global_domain.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
ini_global_domain.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
ini_global_domain.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
ini_global_domain.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
ini_global_domain.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_global_domain.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
ini_global_domain.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
ini_global_domain.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
ini_global_domain.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
ini_global_domain.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
ini_global_domain.for: FCORI_MACROS.h
ini_grid.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
ini_grid.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
ini_grid.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
ini_grid.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_grid.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
ini_grid.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
ini_grid.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
ini_grid.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
ini_grid.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
ini_grid.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
ini_grid.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h MONITOR.h
ini_linear_phisurf.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
ini_linear_phisurf.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
ini_linear_phisurf.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
ini_linear_phisurf.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
ini_linear_phisurf.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
ini_linear_phisurf.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
ini_linear_phisurf.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
ini_linear_phisurf.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_linear_phisurf.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
ini_linear_phisurf.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
ini_linear_phisurf.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
ini_linear_phisurf.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
ini_linear_phisurf.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
ini_linear_phisurf.for: FCORI_MACROS.h SURFACE.h
ini_local_grid.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
ini_local_grid.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h SET_GRID.h
ini_masks_etc.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
ini_masks_etc.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
ini_masks_etc.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
ini_masks_etc.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
ini_masks_etc.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
ini_masks_etc.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_masks_etc.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_masks_etc.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_masks_etc.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_masks_etc.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_masks_etc.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_masks_etc.for: TANPHIATV_MACROS.h FCORI_MACROS.h
ini_mixing.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
ini_mixing.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
ini_mixing.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
ini_mixing.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
ini_mixing.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
ini_mixing.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_mixing.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_mixing.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_mixing.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_mixing.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_mixing.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_mixing.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
ini_mnc_vars.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
ini_mnc_vars.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
ini_mnc_vars.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
ini_mnc_vars.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
ini_mnc_vars.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
ini_mnc_vars.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_mnc_vars.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_mnc_vars.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_mnc_vars.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_mnc_vars.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_mnc_vars.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_mnc_vars.for: TANPHIATV_MACROS.h FCORI_MACROS.h
ini_model_io.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
ini_model_io.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h EESUPPORT.h
ini_model_io.for: /usr/local/include/mpif.h PARAMS.h RESTART.h EEBUFF_SCPU.h
ini_nh_fields.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
ini_nh_fields.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
ini_nh_fields.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
ini_nh_fields.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_nh_fields.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
ini_nh_fields.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
ini_nh_fields.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
ini_nh_fields.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_nh_fields.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_nh_fields.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_nh_fields.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_nh_fields.for: TANPHIATV_MACROS.h FCORI_MACROS.h RESTART.h NH_VARS.h
ini_nh_vars.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
ini_nh_vars.for: EEPARAMS.h PARAMS.h NH_VARS.h
ini_nlfs_vars.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
ini_nlfs_vars.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
ini_nlfs_vars.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
ini_nlfs_vars.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
ini_nlfs_vars.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
ini_nlfs_vars.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_nlfs_vars.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_nlfs_vars.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_nlfs_vars.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_nlfs_vars.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_nlfs_vars.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_nlfs_vars.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
ini_p_ground.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h GRID.h
ini_p_ground.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
ini_p_ground.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
ini_p_ground.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
ini_p_ground.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_p_ground.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_p_ground.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_p_ground.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_p_ground.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_p_ground.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_p_ground.for: TANPHIATV_MACROS.h FCORI_MACROS.h EEPARAMS.h PARAMS.h
ini_p_ground.for: SURFACE.h
ini_parms.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
ini_parms.for: SIZE.h EEPARAMS.h PARAMS.h EOS.h GRID.h GRID_MACROS.h
ini_parms.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
ini_parms.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
ini_parms.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
ini_parms.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_parms.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_parms.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_parms.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_parms.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_parms.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_parms.for: TANPHIATV_MACROS.h FCORI_MACROS.h SET_GRID.h
ini_pressure.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
ini_pressure.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h EOS.h GRID.h
ini_pressure.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
ini_pressure.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
ini_pressure.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
ini_pressure.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_pressure.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_pressure.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_pressure.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_pressure.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_pressure.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_pressure.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
ini_psurf.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
ini_psurf.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
ini_psurf.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
ini_psurf.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_psurf.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
ini_psurf.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
ini_psurf.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
ini_psurf.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
ini_psurf.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
ini_psurf.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
ini_psurf.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
ini_psurf.for: SURFACE.h
ini_salt.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
ini_salt.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
ini_salt.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
ini_salt.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_salt.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
ini_salt.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
ini_salt.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
ini_salt.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
ini_salt.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
ini_salt.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
ini_salt.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
ini_sigma_hfac.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
ini_sigma_hfac.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
ini_sigma_hfac.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
ini_sigma_hfac.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_sigma_hfac.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
ini_sigma_hfac.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
ini_sigma_hfac.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
ini_sigma_hfac.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_sigma_hfac.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_sigma_hfac.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_sigma_hfac.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_sigma_hfac.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
ini_spherical_polar_grid.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
ini_spherical_polar_grid.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h
ini_spherical_polar_grid.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
ini_spherical_polar_grid.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
ini_spherical_polar_grid.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_spherical_polar_grid.for: HFACS_MACROS.h HFACW_MACROS.h
ini_spherical_polar_grid.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
ini_spherical_polar_grid.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
ini_spherical_polar_grid.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_spherical_polar_grid.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
ini_spherical_polar_grid.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
ini_spherical_polar_grid.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
ini_spherical_polar_grid.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_spherical_polar_grid.for: MASKW_MACROS.h MASKS_MACROS.h
ini_spherical_polar_grid.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
ini_spherical_polar_grid.for: FCORI_MACROS.h
ini_theta.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
ini_theta.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
ini_theta.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
ini_theta.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_theta.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
ini_theta.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
ini_theta.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
ini_theta.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
ini_theta.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
ini_theta.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
ini_theta.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
ini_vel.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
ini_vel.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
ini_vel.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
ini_vel.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
ini_vel.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_vel.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
ini_vel.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_vel.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_vel.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
ini_vel.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
ini_vel.for: FCORI_MACROS.h DYNVARS.h
ini_vertical_grid.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
ini_vertical_grid.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
ini_vertical_grid.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
ini_vertical_grid.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
ini_vertical_grid.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
ini_vertical_grid.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
ini_vertical_grid.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
ini_vertical_grid.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
ini_vertical_grid.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
ini_vertical_grid.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
ini_vertical_grid.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
ini_vertical_grid.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
ini_vertical_grid.for: TANPHIATV_MACROS.h FCORI_MACROS.h
initialise_fixed.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
initialise_fixed.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
initialise_varia.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
initialise_varia.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h DYNVARS.h
initialise_varia.for: SURFACE.h
integr_continuity.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
integr_continuity.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h DYNVARS.h
integr_continuity.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
integr_continuity.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
integr_continuity.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
integr_continuity.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
integr_continuity.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
integr_continuity.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
integr_continuity.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
integr_continuity.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
integr_continuity.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
integr_continuity.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
integr_continuity.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
integr_continuity.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h FFIELDS.h
integrate_for_w.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
integrate_for_w.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
integrate_for_w.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
integrate_for_w.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
integrate_for_w.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
integrate_for_w.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
integrate_for_w.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
integrate_for_w.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
integrate_for_w.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
integrate_for_w.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
integrate_for_w.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
integrate_for_w.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
load_fields_driver.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
load_fields_driver.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h FFIELDS.h
load_grid_spacing.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
load_grid_spacing.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
load_grid_spacing.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
load_grid_spacing.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
load_grid_spacing.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
load_grid_spacing.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
load_grid_spacing.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
load_grid_spacing.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
load_grid_spacing.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
load_grid_spacing.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
load_grid_spacing.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
load_grid_spacing.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
load_grid_spacing.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
load_grid_spacing.for: FCORI_MACROS.h SET_GRID.h
load_ref_files.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
load_ref_files.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
load_ref_files.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
load_ref_files.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
load_ref_files.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
load_ref_files.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
load_ref_files.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
load_ref_files.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
load_ref_files.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
load_ref_files.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
load_ref_files.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
load_ref_files.for: TANPHIATV_MACROS.h FCORI_MACROS.h
main_do_loop.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
main_do_loop.for: CPP_EEMACROS.h OBCS_OPTIONS.h GAD_OPTIONS.h SIZE.h
main_do_loop.for: EEPARAMS.h PARAMS.h
momentum_correction_step.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
momentum_correction_step.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
momentum_correction_step.for: DYNVARS.h
packages_boot.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
packages_boot.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
packages_check.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
packages_check.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
packages_error_msg.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
packages_error_msg.for: EEPARAMS.h
packages_init_fixed.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
packages_init_fixed.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
packages_init_variables.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
packages_init_variables.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
packages_print_msg.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
packages_print_msg.for: EEPARAMS.h
packages_readparms.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
packages_readparms.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
packages_unused_msg.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
packages_unused_msg.for: EEPARAMS.h
packages_write_pickup.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
packages_write_pickup.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
packages_write_pickup.for: RESTART.h
plot_field.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
plot_field.for: EEPARAMS.h PARAMS.h
post_cg3d.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h EEPARAMS.h
post_cg3d.for: PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
post_cg3d.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
post_cg3d.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
post_cg3d.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
post_cg3d.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
post_cg3d.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
post_cg3d.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
post_cg3d.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
post_cg3d.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
post_cg3d.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h DYNVARS.h
pre_cg3d.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
pre_cg3d.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
pre_cg3d.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
pre_cg3d.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
pre_cg3d.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
pre_cg3d.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
pre_cg3d.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
pre_cg3d.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
pre_cg3d.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
pre_cg3d.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
pre_cg3d.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
pre_cg3d.for: FFIELDS.h DYNVARS.h
pressure_for_eos.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
pressure_for_eos.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
pressure_for_eos.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
pressure_for_eos.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
pressure_for_eos.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
pressure_for_eos.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
pressure_for_eos.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
pressure_for_eos.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
pressure_for_eos.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
pressure_for_eos.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
pressure_for_eos.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
pressure_for_eos.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
pressure_for_eos.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
read_pickup.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
read_pickup.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h RESTART.h
read_pickup.for: DYNVARS.h SURFACE.h FFIELDS.h GAD.h
remove_mean.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
remove_mean.for: EEPARAMS.h PARAMS.h
reset_nlfs_vars.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
reset_nlfs_vars.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
reset_nlfs_vars.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
reset_nlfs_vars.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
reset_nlfs_vars.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
reset_nlfs_vars.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
reset_nlfs_vars.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
reset_nlfs_vars.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
reset_nlfs_vars.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
reset_nlfs_vars.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
reset_nlfs_vars.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
reset_nlfs_vars.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
rotate_spherical_polar_grid.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
rotate_spherical_polar_grid.for: SIZE.h EEPARAMS.h PARAMS.h
rotate_uv2en.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h EEPARAMS.h
rotate_uv2en.for: SIZE.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
rotate_uv2en.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
rotate_uv2en.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
rotate_uv2en.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
rotate_uv2en.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
rotate_uv2en.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
rotate_uv2en.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
rotate_uv2en.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
rotate_uv2en.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
rotate_uv2en.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
rotate_uv2en.for: TANPHIATV_MACROS.h FCORI_MACROS.h
salt_integrate.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
salt_integrate.for: CPP_EEMACROS.h GAD_OPTIONS.h SIZE.h EEPARAMS.h PARAMS.h
salt_integrate.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
salt_integrate.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
salt_integrate.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
salt_integrate.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
salt_integrate.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
salt_integrate.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
salt_integrate.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
salt_integrate.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
salt_integrate.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
salt_integrate.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
salt_integrate.for: DYNVARS.h RESTART.h GAD.h GAD_SOM_VARS.h
seawater.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
set_defaults.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
set_defaults.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h SET_GRID.h
set_grid_factors.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
set_grid_factors.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
set_grid_factors.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
set_grid_factors.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
set_grid_factors.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
set_grid_factors.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
set_grid_factors.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
set_grid_factors.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
set_grid_factors.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
set_grid_factors.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
set_grid_factors.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
set_grid_factors.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
set_grid_factors.for: TANPHIATV_MACROS.h FCORI_MACROS.h
set_parms.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
set_parms.for: MOM_COMMON_OPTIONS.h SIZE.h EEPARAMS.h PARAMS.h EOS.h
set_parms.for: MOM_VISC.h
set_ref_state.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
set_ref_state.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
set_ref_state.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
set_ref_state.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
set_ref_state.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
set_ref_state.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
set_ref_state.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
set_ref_state.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
set_ref_state.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
set_ref_state.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
set_ref_state.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
set_ref_state.for: TANPHIATV_MACROS.h FCORI_MACROS.h EOS.h
solve_for_pressure.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
solve_for_pressure.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
solve_for_pressure.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
solve_for_pressure.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
solve_for_pressure.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
solve_for_pressure.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
solve_for_pressure.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
solve_for_pressure.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
solve_for_pressure.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
solve_for_pressure.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
solve_for_pressure.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
solve_for_pressure.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
solve_for_pressure.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
solve_for_pressure.for: FCORI_MACROS.h SURFACE.h FFIELDS.h DYNVARS.h
solve_for_pressure.for: SOLVE_FOR_PRESSURE.h
solve_pentadiagonal.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
solve_pentadiagonal.for: EEPARAMS.h
solve_tridiagonal.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
solve_tridiagonal.for: EEPARAMS.h
solve_uv_tridiago.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
solve_uv_tridiago.for: EEPARAMS.h
state_summary.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
state_summary.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
state_summary.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
state_summary.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
state_summary.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
state_summary.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
state_summary.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
state_summary.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
state_summary.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
state_summary.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
state_summary.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
state_summary.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
swfrac.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
taueddy_init_varia.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
taueddy_init_varia.for: EEPARAMS.h PARAMS.h FFIELDS.h
taueddy_tendency_apply.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
taueddy_tendency_apply.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
taueddy_tendency_apply.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
taueddy_tendency_apply.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
taueddy_tendency_apply.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
taueddy_tendency_apply.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
taueddy_tendency_apply.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
taueddy_tendency_apply.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
taueddy_tendency_apply.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
taueddy_tendency_apply.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
taueddy_tendency_apply.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
taueddy_tendency_apply.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
taueddy_tendency_apply.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
taueddy_tendency_apply.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
taueddy_tendency_apply.for: TANPHIATV_MACROS.h FCORI_MACROS.h FFIELDS.h
temp_integrate.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
temp_integrate.for: CPP_EEMACROS.h GAD_OPTIONS.h SIZE.h EEPARAMS.h PARAMS.h
temp_integrate.for: GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
temp_integrate.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
temp_integrate.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
temp_integrate.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
temp_integrate.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
temp_integrate.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
temp_integrate.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
temp_integrate.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
temp_integrate.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
temp_integrate.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
temp_integrate.for: DYNVARS.h RESTART.h GAD.h GAD_SOM_VARS.h TIMEAVE_STATV.h
temp_integrate.for: TIMEAVE_OPTIONS.h
the_main_loop.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
the_main_loop.for: CPP_EEMACROS.h OBCS_OPTIONS.h GAD_OPTIONS.h SIZE.h
the_main_loop.for: EEPARAMS.h PARAMS.h
the_model_main.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
the_model_main.for: CPP_EEMACROS.h AD_CONFIG.h SIZE.h EEPARAMS.h PARAMS.h
the_model_main.for: DYNVARS.h
thermodynamics.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
thermodynamics.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h RESTART.h
thermodynamics.for: DYNVARS.h GRID.h GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h
thermodynamics.for: DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
thermodynamics.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
thermodynamics.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
thermodynamics.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
thermodynamics.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
thermodynamics.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
thermodynamics.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
thermodynamics.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
thermodynamics.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
thermodynamics.for: SURFACE.h FFIELDS.h GAD.h
timestep.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
timestep.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
timestep.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
timestep.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
timestep.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
timestep.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
timestep.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
timestep.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
timestep.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
timestep.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
timestep.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
timestep.for: RESTART.h DYNVARS.h
timestep_tracer.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
timestep_tracer.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
timestep_tracer.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
timestep_tracer.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
timestep_tracer.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
timestep_tracer.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
timestep_tracer.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
timestep_tracer.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
timestep_tracer.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
timestep_tracer.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h RA_MACROS.h
timestep_tracer.for: RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
timestep_tracer.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h FCORI_MACROS.h
timestep_wvel.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
timestep_wvel.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
timestep_wvel.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
timestep_wvel.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
timestep_wvel.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
timestep_wvel.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
timestep_wvel.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
timestep_wvel.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
timestep_wvel.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
timestep_wvel.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
timestep_wvel.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
timestep_wvel.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h NH_VARS.h
tracers_correction_step.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
tracers_correction_step.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h
tracers_correction_step.for: DYNVARS.h GAD.h
tracers_iigw_correction.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h
tracers_iigw_correction.for: SIZE.h EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h
tracers_iigw_correction.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
tracers_iigw_correction.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h
tracers_iigw_correction.for: DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
tracers_iigw_correction.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
tracers_iigw_correction.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
tracers_iigw_correction.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h
tracers_iigw_correction.for: RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
tracers_iigw_correction.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
tracers_iigw_correction.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h
tracers_iigw_correction.for: XC_MACROS.h YC_MACROS.h RA_MACROS.h RAW_MACROS.h
tracers_iigw_correction.for: RAS_MACROS.h MASKW_MACROS.h MASKS_MACROS.h
tracers_iigw_correction.for: TANPHIATU_MACROS.h TANPHIATV_MACROS.h
tracers_iigw_correction.for: FCORI_MACROS.h DYNVARS.h
turnoff_model_io.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
turnoff_model_io.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h OBCS_PARAMS.h
update_cg2d.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
update_cg2d.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
update_cg2d.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
update_cg2d.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
update_cg2d.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
update_cg2d.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
update_cg2d.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
update_cg2d.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
update_cg2d.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
update_cg2d.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
update_cg2d.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
update_cg2d.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h CG2D.h
update_etah.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
update_etah.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h DYNVARS.h GRID.h
update_etah.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
update_etah.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
update_etah.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
update_etah.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
update_etah.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
update_etah.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
update_etah.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
update_etah.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
update_etah.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
update_etah.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
update_etaws.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
update_etaws.for: EEPARAMS.h PARAMS.h DYNVARS.h GRID.h GRID_MACROS.h
update_etaws.for: DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h
update_etaws.for: DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h
update_etaws.for: HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
update_etaws.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
update_etaws.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
update_etaws.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
update_etaws.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
update_etaws.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
update_etaws.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
update_etaws.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
update_masks_etc.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
update_masks_etc.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
update_masks_etc.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
update_masks_etc.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
update_masks_etc.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h
update_masks_etc.for: HFACW_MACROS.h RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h
update_masks_etc.for: RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
update_masks_etc.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
update_masks_etc.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h
update_masks_etc.for: RECIP_HFACC_MACROS.h RECIP_HFACS_MACROS.h
update_masks_etc.for: RECIP_HFACW_MACROS.h XC_MACROS.h YC_MACROS.h
update_masks_etc.for: RA_MACROS.h RAW_MACROS.h RAS_MACROS.h MASKW_MACROS.h
update_masks_etc.for: MASKS_MACROS.h TANPHIATU_MACROS.h TANPHIATV_MACROS.h
update_masks_etc.for: FCORI_MACROS.h SURFACE.h
update_r_star.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
update_r_star.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
update_r_star.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
update_r_star.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
update_r_star.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
update_r_star.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
update_r_star.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
update_r_star.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
update_r_star.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
update_r_star.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
update_r_star.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
update_r_star.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
update_sigma.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
update_sigma.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
update_sigma.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
update_sigma.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
update_sigma.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
update_sigma.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
update_sigma.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
update_sigma.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
update_sigma.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
update_sigma.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
update_sigma.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
update_sigma.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
update_surf_dr.for: CPP_OPTIONS.h CPP_EEOPTIONS.h CPP_EEMACROS.h SIZE.h
update_surf_dr.for: EEPARAMS.h PARAMS.h GRID.h GRID_MACROS.h DXC_MACROS.h
update_surf_dr.for: DXF_MACROS.h DXG_MACROS.h DXV_MACROS.h DYC_MACROS.h
update_surf_dr.for: DYF_MACROS.h DYG_MACROS.h DYU_MACROS.h HFACC_MACROS.h
update_surf_dr.for: HFACS_MACROS.h HFACW_MACROS.h RECIP_DXC_MACROS.h
update_surf_dr.for: RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h RECIP_DXV_MACROS.h
update_surf_dr.for: RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h RECIP_DYG_MACROS.h
update_surf_dr.for: RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
update_surf_dr.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
update_surf_dr.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
update_surf_dr.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
update_surf_dr.for: TANPHIATV_MACROS.h FCORI_MACROS.h SURFACE.h
write_grid.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
write_grid.for: CPP_EEMACROS.h AD_CONFIG.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
write_grid.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
write_grid.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
write_grid.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
write_grid.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
write_grid.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
write_grid.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
write_grid.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
write_grid.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
write_grid.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
write_grid.for: TANPHIATV_MACROS.h FCORI_MACROS.h
write_pickup.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
write_pickup.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h RESTART.h
write_pickup.for: DYNVARS.h SURFACE.h FFIELDS.h GAD.h
write_state.for: PACKAGES_CONFIG.h CPP_OPTIONS.h CPP_EEOPTIONS.h
write_state.for: CPP_EEMACROS.h SIZE.h EEPARAMS.h PARAMS.h GRID.h
write_state.for: GRID_MACROS.h DXC_MACROS.h DXF_MACROS.h DXG_MACROS.h
write_state.for: DXV_MACROS.h DYC_MACROS.h DYF_MACROS.h DYG_MACROS.h
write_state.for: DYU_MACROS.h HFACC_MACROS.h HFACS_MACROS.h HFACW_MACROS.h
write_state.for: RECIP_DXC_MACROS.h RECIP_DXF_MACROS.h RECIP_DXG_MACROS.h
write_state.for: RECIP_DXV_MACROS.h RECIP_DYC_MACROS.h RECIP_DYF_MACROS.h
write_state.for: RECIP_DYG_MACROS.h RECIP_DYU_MACROS.h RECIP_HFACC_MACROS.h
write_state.for: RECIP_HFACS_MACROS.h RECIP_HFACW_MACROS.h XC_MACROS.h
write_state.for: YC_MACROS.h RA_MACROS.h RAW_MACROS.h RAS_MACROS.h
write_state.for: MASKW_MACROS.h MASKS_MACROS.h TANPHIATU_MACROS.h
write_state.for: TANPHIATV_MACROS.h FCORI_MACROS.h DYNVARS.h
